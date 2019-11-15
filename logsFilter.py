import json
from urllib2 import urlopen 
import string
import sys
import re
import time

with open (sys.argv[1], "r") as myfile:
    logFile=myfile.read() 

ipTable = re.findall( "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", logFile ) 
ipTable = list(set(ipTable))
url = 'http://ipinfo.io/' 

for ip in ipTable:

    if not ip.startswith("0.") and ip.startswith("0"): 
        ip = ip[1:] 
    try:
        time.sleep(0.1)
        response = urlopen(url+str(ip)+str("/json"))
        data = json.load(response)
        if 'country' in data: 
            country=data['country']
        else:
            country="N/A"	
        if(len(sys.argv)==3):

            if(sys.argv[2]==country):
                print json.dumps(data,indent=1) 
            else:
                if(sys.argv[2]!= "-"+country and not('bogon' in data)):
                    print json.dumps(data,indent=1) 
        else:
            print json.dumps(data,indent=1)

    except Exception as inst:
        print type (inst)


