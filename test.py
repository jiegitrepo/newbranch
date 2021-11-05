#!/usr/bin/env python3

import requests
import json
import os


here = os.path.abspath(os.path.dirname(__file__))
here2 = os.path.join(here, "token.txt")

with open(here2) as file:
	token = file.read()

#print(token.rstrip("\n\r"))


response = requests.get('https://webexapis.com/v1/teams', headers={'Authorization':"Bearer {}".format(token.rstrip("\n\r"))})
print(response)
print(response.json())

print(response.status_code)
#print(here2)
