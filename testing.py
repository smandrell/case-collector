# import urllib3.request

import urllib.request
import json

import requests


url = 'http://apps.marincounty.org/BeaconRoa/BeaconROASearch.aspx'

search_data = {'txtCaseType': '', 'txtCaseNumber': '%123', 'txtCaseName': 'N', 'txtPartName': ''}

# data = urllib.urlencode(values)
# req = request(url, data)
# response = urllib2.urlopen(req)
# the_page = response.read()

# data = urllib3.request.urlencode(search_data)
#
# self = urllib3.request.RequestMethods()
#
# req = self.request(method='post', url=url, fields=search_data)

##### GOT SOMETHING HERE

# request = urllib.request.Request(url, data=bytes(json.dumps(search_data), encoding='utf-8'), method='POST')
#
# response = urllib.request.urlopen(request)
#
# print(response.read().decode('utf-8'))

r = requests.post(url, data=search_data)

with open("request_results.html", "wb") as f:
    f.write(r.content)

