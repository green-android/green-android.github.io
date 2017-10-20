#coding:utf-8
#!/usr/bin/python

import json

'''
  <div class="col-xs-12 col-md-6 col-lg-4">
    <a class="card bg-gray-light p-4 mb-4 d-block clearfix" target="_blank" href="http://www.coolapk.com/apk/com.kongzue.paywhere">
      <img class="float-left rounded-1" src="assets/images/app_paywhere.png" style="width: 48px;" alt="app-icon">
      <div class="pl-3 float-left">
        <div class="text-black text-bold mt-1">花哪儿记账</div>
        <div class="f6 text-mono">简单、纯粹的记账应用</div>
      </div>
    </a>
  </div>

'''

with open("apps.json",'r') as load_f:
    load_dict = json.load(load_f)
    for app in load_dict:
    	print('<div class="col-xs-12 col-md-6 col-lg-4">')

    	print('\t<a class="card bg-gray-light p-4 mb-4 d-block clearfix" target="_blank" href="' + app["downloadUrl"] + '">')

    	print('\t\t<img class="float-left rounded-1" src="assets/icons/' + app["packageName"] + '.png" style="width: 48px;" alt="app-icon"/>')

    	print('\t\t<div class="pl-3 float-left">')

    	print('\t\t\t<div class="text-black text-bold mt-1">' + app["appName"] + '</div>')
    	print('\t\t\t<div class="f6 text-mono">' + app["slogan"] + '</div>')
    	
    	print('\t\t</div>')
    	
    	print('\t</a>')

    	print('</div>')
    	#urllib.urlretrieve(app["iconUrl"], ("icons/" + app["packageName"] + ".png"))