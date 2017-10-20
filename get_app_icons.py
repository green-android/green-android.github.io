#coding:utf-8
#!/usr/bin/python

import json
import urllib

with open("apps.json",'r') as load_f:
    load_dict = json.load(load_f)
    for app in load_dict:
    	print(app["iconUrl"])
    	urllib.urlretrieve(app["iconUrl"], ("icons/" + app["packageName"] + ".png"))