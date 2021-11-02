#!/usr/bin/env python3
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os
from pprint import pprint


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
	file_content = file.read()


json_data = json.loads(file_content)

# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.

pprint(json_data)


for interface in json_data["ietf-interfaces:interfaces"]["interface"]:
	print(interface["name"])
	print(interface["ietf-ip:ipv4"]["address"][0]["ip"])
	print(interface["ietf-ip:ipv4"]["address"][0]["netmask"])
	print("\n")
