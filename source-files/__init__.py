# -*- coding: future_fstrings -*-
# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import string
import json

# /api/login
# /api/activeCalls
# /api/ExtensionList
# /api/SystemStatus/GetSingleStatus
# /api/SystemStatus
# /api/UpdateChecker/GetFromParams
# /api/TrunkList

print("<<<3CX>>>")
api_username = 'admin'
api_password = 'Jer0me3CX2021!'
base_url = 'https://solutionsaccestechnologies.my3cx.ca'

headers = {'Content-type': 'application/json'}
data = {'Username': api_username, 'Password': api_password}
try:
    r_auth = requests.post(f'{base_url}/api/login', data=json.dumps(data), headers=headers)
    authcookies = r_auth.cookies
except:
    print(f'Unable to connect to {base_url}')
    exit(1)

if r_auth.status_code != 200 or r_auth.text != "AuthSuccess":
    # print(f'Unable to connect to {base_url}')
    print(r_auth.text)
    exit(1)

r_activeCalls = requests.get(f'{base_url}/api/activeCalls', cookies=authcookies)
activeCalls = json.loads(r_activeCalls.text)
# print(activeCalls)

r_extensionList = requests.get(f'{base_url}/api/ExtensionList', cookies=authcookies)
extensionList = json.loads(r_extensionList.text)
# print(extensionList)

r_singleStatus = requests.get(f'{base_url}/api/SystemStatus/GetSingleStatus', cookies=authcookies)
singleStatus = json.loads(r_singleStatus.text)
# print(singleStatus)

r_systemStatus = requests.get(f'{base_url}/api/SystemStatus', cookies=authcookies)
systemStatus = json.loads(r_systemStatus.text)
# print(systemStatus)

r_updateStatus = requests.get(f'{base_url}/api/UpdateChecker/GetFromParams', cookies=authcookies)
updateStatus = json.loads(r_updateStatus.text)
# print(updateStatus)

r_trunkStatus = requests.get(f'{base_url}/api/TrunkList', cookies=authcookies)
trunkStatus = json.loads(r_trunkStatus.text)
# print(trunkStatus)

r_additionalStatus = requests.get(f'{base_url}/api/SystemStatus/AdditionalStatus', cookies=authcookies)
additionalStatus = json.loads(r_additionalStatus.text)
# print(additionalStatus)

# /api/TrunkList

nbActiveCalls = systemStatus['CallsActive']
nbCallLimit = systemStatus['MaxSimCalls']
firewallStatus = "OK" if singleStatus['Health']['Firewall'] is True else "Error"
unregisteredSystemExtension = "OK" if systemStatus['HasUnregisteredSystemExtensions'] is False else "Error"
services = "OK" if systemStatus['HasNotRunningServices'] is False else "Error"
updatesAvailable = "Up to date" if updateStatus['tcxUpdate'] == '[]' else "Updates available!"
nbTrunks = systemStatus['TrunksTotal']
nbRegisteredTrunks = systemStatus['TrunksRegistered']
recordingQuota = additionalStatus['RecordingQuota']
recordingUsed =  additionalStatus['RecordingUsedSpace']

print(f'Active Calls: {nbActiveCalls}')
print(f'Max Calls: {nbCallLimit}')
print(f'Firewall: {firewallStatus}')
print(f'System Extensions: {unregisteredSystemExtension}')
print(f'Services: {services}')
print(f'Updates available: {updatesAvailable}')
print(f'Trunks: {nbTrunks}')
print(f'Registered Trunks: {nbRegisteredTrunks}')
print(f'Recording Quota: {recordingQuota}')
print(f'Recording Used Space: {recordingUsed}')
