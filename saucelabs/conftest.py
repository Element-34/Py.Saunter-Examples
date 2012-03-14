# Copyright 2011 Element 34
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import saunter.ConfigWrapper

if saunter.ConfigWrapper.ConfigWrapper().config.getboolean("SauceLabs", "ondemand"):
    import json

cf = saunter.ConfigWrapper.ConfigWrapper().config

import os.path
import time
import requests
import urllib2

import py
import _pytest

from saunter.SeleniumWrapper import SeleniumWrapper as wrapper

class AdvancedReport(_pytest.runner.TestReport):
    def __init__(self, nodeid, location, marks, outcome, longrepr, when):
        super(AdvancedReport, self).__init__(nodeid, location, marks, outcome, longrepr, when)
                
    def __repr__(self):
        return "<AdvancedReport %r when=%r outcome=%r>" % (
            self.nodeid, self.when, self.outcome)

def pytest_runtest_makereport(item, call):
    when = call.when
    # get the MarkInfo objects since 'keyword' is essentially useless.
    marks = []
    for keyword in item.keywords:
        if isinstance(item.keywords[keyword], _pytest.mark.MarkInfo):
            marks.append(keyword)

    excinfo = call.excinfo
    if not call.excinfo:
        outcome = "passed"
        longrepr = None
    else:
        excinfo = call.excinfo
        if not isinstance(excinfo, py.code.ExceptionInfo):
            outcome = "failed"
            longrepr = excinfo
        elif excinfo.errisinstance(py.test.skip.Exception):
            outcome = "skipped"
            r = excinfo._getreprcrash()
            longrepr = (str(r.path), r.lineno, r.message)
        else:
            outcome = "failed"
            if call.when == "call":
                longrepr = item.repr_failure(excinfo)
            else: # exception in setup or teardown
                longrepr = item._repr_failure_py(excinfo)
    return AdvancedReport(item.nodeid, item.location, marks, outcome, longrepr, when)

def fetch_artifact(which):
    sauce_session = wrapper().connection.sauce_session
    which_url = "https://saucelabs.com/rest/%s/jobs/%s/results/%s" % (cf.get("SauceLabs", "username"), sauce_session, which)
    code = 404
    timeout = 0
    while code in [401, 404]:
        r = requests.get(which_url, auth = (cf.get("SauceLabs", "username"), cf.get("SauceLabs", "key")))
        try:
            code = r.status_code
            r.raise_for_status()
        except urllib2.HTTPError, e:
            time.sleep(4)

    artifact = open(os.path.join(os.path.dirname(__file__), "logs", which), "wb")
    artifact.write(r.content)

def pytest_runtest_logreport(report):
    if report.when != "teardown":
        return
    
    w = wrapper()
    try:
        c = w.connection
        if c.running:
            c.stop()
    except AttributeError:
        pass

    if cf.getboolean("SauceLabs", "ondemand"):
        # session couldn't be established for some reason
        if not hasattr(c, "sauce_session"):
            print("hmmm")
            return
        sauce_session = c.sauce_session
        
        j = {}
    
        # name
        names = report.nodeid.split("::")
        names[0] = names[0].replace("/", '.')
        names = tuple(names)
        d = {}
        names = [x.replace(".py", "") for x in names if x != "()"]
        classnames = names[:-1]
        d['classname'] = ".".join(classnames)
        d['name'] = py.xml.escape(names[-1])
        attrs = ['%s="%s"' % item for item in sorted(d.items())]
        j["name"] = d['name']
    
        # result
        if report.passed:
            j["passed"] = True
        else:
            j["passed"] = False

        # tags
        j["tags"] = report.keywords
        
        # update
        which_url = "https://saucelabs.com/rest/v1/%s/jobs/%s" % (cf.get("SauceLabs", "username"), sauce_session)
        r = requests.put(which_url,
                         data=json.dumps(j),
                         headers={"Content-Type": "application/json"},
                         auth=(cf.get("SauceLabs", "username"), cf.get("SauceLabs", "key")))
        r.raise_for_status()

        if cf.getboolean("SauceLabs", "get_video"):
            fetch_artifact("video.flv")
        
        if cf.getboolean("SauceLabs", "get_log"):
            fetch_artifact("selenium-server.log")