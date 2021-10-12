import requests
import json

resAPI = "" #check email
response = requests.get(resAPI, {})
resp = json.loads(response.content)
survey = resp["body"]
print("=="*5 + " Aggregate results " + "=="*5)
print(survey['Aggregate'])
print("=="*5 + " Responses " + "=="*5)
print(survey['Responses'])
