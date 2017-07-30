import requests
import requests_oauthlib
import pycurl
import json
import time
import sqlite3 as sqlite
import math
import random

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

try:
    fevent = open("eventnew.txt","r")
    # events_dic = json.loads(fevent.read())
except:
    events_dic=dict()
    count =0
    for i in range(12):
        for j in range(3):
            temp_url = "https://events.umich.edu/list/json?filter=all&range=2017-0{}-{}to2017-0{}-{}".format(i+1,j*10+1,i+1,j*10+11)
            r = json.loads(requests.get(temp_url).text)
            time.sleep(5)
            for event in r:
                if event not in events_dic:
                    events_dic[event] = r[event]
                    count +=1

    f = open("event_cache.txt","w")
    f.write(json.dumps(events_dic))
    f.close()
    print count
