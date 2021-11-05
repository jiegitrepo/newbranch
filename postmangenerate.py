#!/usr/bin/env python3

import requests

url = "https://deckofcardsapi.com/api/deck/r7wbr68ri5f8/draw/?count=6"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)

deck = response.json()
deck_id = deck['deck_id']

print(deck_id)
