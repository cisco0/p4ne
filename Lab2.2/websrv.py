
#from flask import Flask
from flask import *
import sys
import glob
import re

list1=[]
hosts = {}
ip = {}

def cl(s):
    s = re.match(' ip address ([0-9.]+) ([0-9.]+)', m)
    if s:
        return ('IP', s.group(1), s.group(2))
    s = re.match('^hostname (.+)', m)
    if s:
        return ("HOST", s.groups())
    s = re.match('^interface (.+)', m)
    if s:
        return ("INT", s.groups())
    else:
        return ("UNCLASSIFIED", )
current_host = ""
x = glob.glob("C:\\Users\\va.martynov\\Seafile\\p4ne_training\\config_files\\*.txt")
for i in x:
    with open(i) as f:
        strlist=list(f)
       # print (strlist)
        for m in strlist:

            a = cl(m)
            if a[0] == "HOST":
                hosts[a[1]] = {"name": a[1]}
                current_host = a[1]
            if a[0] == "IP" and current_host:
                    hosts[current_host]["ip"] = a[1]


app = Flask(__name__)

@app.route('/')
def index():
 return "123321"
@app.route('/page1')
def page():
 return jsonify(str(sys.__dict__))
@app.route('/config')
@app.route('/config/')
def config():
  return jsonify(list(ip.keys()))
@app.route('/config/ip')
def configip():
  return jsonify(list(hosts.keys()))
@app.route('/config/<hostname>')
def ip_info(hostname):
    for h in hosts.keys():
        if hosts[h]['name'][0] == hostname:
            return jsonify(hosts[h]['ip'])
    return jsonify('Not found')


if __name__ == "__main__":
    print(hosts)
    app.run(debug=True)
