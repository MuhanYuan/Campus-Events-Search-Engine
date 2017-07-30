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

with open("event_cache.txt","r") as datafile:
    event_json = datafile.read()
    events_dic = json.loads(event_json)

tag_dic = {}

for event in events_dic:
    try:
        for i in events_dic[event]["tags"]:
            if i not in tag_dic:
                tag_dic[i] = 1
            else:
                tag_dic[i] += 1
    except:
        pass

# print pretty(tag_dic)

outfile = open("tags.txt","w")
outfile.write(json.dumps(tag_dic))
outfile.close()
