import requests
import json
import os

surveyAPI = "" #check email
print("working from where survey, pls enter 1 or 0 as response, 1 beign yes\n\n")
wfh = int(input("Do you prefer complete WFH? "))
if wfh not in [0, 1]:
   print("Bad input %d. Just 1 or 0" %wfh)
   os._exit(-1)

hw = int(input("Do you prefer Hybrid work? "))
if hw not in [0, 1]:
   print("Bad input %d. just 1 or 0" %hw)
   os._exit(-1)

ow = int(input("Do you prefer complete office? "))
if ow not in [0, 1]:
   print("Bad input %d. Just 1 or 0" %ow)
   os._exit(-1)

print("Thanks for participating in survey, uploading your responses")

data = {
  "responses": {
    "Permanent WFH": wfh,
    "Hybrid": hw,
    "Office": ow,
  }
}
response = requests.post(surveyAPI, json.dumps(data))
resp = json.loads(response.content)
print(resp)
survey = resp["body"]
print(survey)
