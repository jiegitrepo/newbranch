#!/usr/bin/env python3

import requests
import json
from requests.auth import HTTPBasicAuth
import os
import sys

requests.packages.urllib3.disable_warnings()


DNAC="sandboxdnac.cisco.com"
DNAC_USER="devnetuser"
DNAC_PASSWORD="Cisco123!"
DNAC_PORT="443"
paths = ""


def get_auth_token(controller_ip=DNAC, username=DNAC_USER, password=DNAC_PASSWORD):
    """ Authenticates with controller and returns a token to be used in subsequent API invocations
    """

    login_url = "https://{0}:{1}/dna/system/api/v1/auth/token".format(controller_ip, DNAC_PORT)
# Change verify to TRUE
    result = requests.post(url=login_url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD), verify=True)
    result.raise_for_status()

    token = result.json()["Token"]
#    print(resultss)
    tokens = result.json()
  #  print(result.headers)
  #  print(token) 
  # print(tokens)
    return {
        "controller_ip": controller_ip,
        "token": token
    }


def create_url(path, controller_ip=DNAC):
    """ Helper function to create a DNAC API endpoint URL
    """
    print("3")
    return "https://%s:%s/api/v1/%s" % (controller_ip, DNAC_PORT, path)


def get_url(url):
    url = create_url(url)
    print("2")
    token = get_auth_token()
    headers = {'X-auth-token' : token['token']}
#change very to TRUE
    try:
        response = requests.get(url, headers=headers, verify=True)
        tokenss = response.json()
       # print(tokenss)
    except requests.exceptions.RequestException as cerror:
        print("Error processing request", cerror)
        sys.exit(1)

    
    return response.json()


def list_network_devices():
    print("1")
    return get_url("network-device")

def ip_to_id(ip):
    return get_url("network-device/ip-address/%s" % ip)['response']['id']

def get_modules(id):
   return get_url("network-device/module?deviceId=%s" % id)


def print_info(modules):
    print("{0:30}{1:15}{2:25}{3:5}".format("Module Name","Serial Number","Part Number","Is Field Replaceable?"))
    for module in modules['response']:
        print("{moduleName:30}{serialNumber:15}{partNumber:25}{moduleType:5}".format(moduleName=module['name'],
                                                           serialNumber=module['serialNumber'],
                                                           partNumber=module['partNumber'],
                                                           moduleType=module['isFieldReplaceable']))





if __name__ == "__main__":
    response = list_network_devices()
    print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
        format("hostname","mgmt IP","serial",
        "platformId","SW Version","role","Uptime"))

    for device in response['response']:
        uptime = "N/A" if device['upTime'] is None else device['upTime']
        print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
            format(device['hostname'],
                    device['managementIpAddress'],
                    device['serialNumber'],
                    device['platformId'],
                    device['softwareVersion'],
                    device['role'],uptime))


'''if __name__ == "__main__":
   if len(sys.argv) > 1:
       dev_id = ip_to_id(sys.argv[1])
       modules = get_modules(dev_id)
       print_info(modules)
   else:
       print("Usage: %s device_ip" % sys.argv[0])
'''