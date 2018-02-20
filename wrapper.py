import urllib, urllib2
import sys
import os
import requests
import urllib

opt1 = sys.argv[1]
appName = sys.argv[2]
opt2 = sys.argv[3]
appID = sys.argv[4]
opt3 = sys.argv[5]
token = sys.argv[6]

url = 'https://appsecure.accenture.com/api/scan_binary/'

path = os.environ['JENKINS_HOME']+'/jobs/'+os.environ['JOB_NAME']+'/workspace/'+appName

files = {'binaryFile': open(path,'rb')}

values = {
		  'Uid' : appID,
           }

authtoken = "JWT "+str(token)

headers = { "Authorization" : authtoken }

response = requests.post(url, data=values,files=files,headers=headers)

print response.json()
