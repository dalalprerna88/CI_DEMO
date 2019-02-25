import sys
import os
import requests

appName = sys.argv[1]
appID = "1450aa62fbe21fcd180f44ed241203f4"
token =  "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0NCwiZW1haWwiOiJwcmVybmEuZGFsYWxAYWNjZW50dXJlLmNvbSIsInVzZXJuYW1lIjoiZGFsYWxwcmVybmE4OCIsImV4cCI6MTU1MTE4MjkyOCwib3JpZ19pYXQiOjE1NTEwOTY1Mjh9.P_XU6wCTw2Em72vU0whKlcEaMePnh2aq6RcDNcEjmwc"
token = str(token).strip()
appID = str(appID).strip()

url = 'https://appsecure.accenture.com/api/scan_binary/'

path = os.environ['JENKINS_HOME']+'/jobs/'+os.environ['JOB_NAME']+'/workspace/'+appName

files = {'binaryFile': open(path,'rb')}

values = {'Uid': appID}

authtoken = "JWT "+str(token)

headers = { "Authorization" : authtoken }

response = requests.post(url, data=values,files=files,headers=headers)

print (response.json())
