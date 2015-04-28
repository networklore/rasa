import json

import requests
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'RASA'
}



class ASA(object):


    def __init__(self, device, username, password):

        self.device = device
        self.username = username
        self.password = password

        self.cred = HTTPBasicAuth(self.username, self.password)

    def _get(self, request):
        url = 'https://' + self.device + '/api/' + request
        data = requests.get(url,headers=HEADERS,auth=self.cred, verify=False)
        #return data
        if data.status_code == 200:
            return data.json()
        else:
            return {}        

    def _patch(self, request, data):
        url = 'https://' + self.device + '/api/' + request
        data = requests.patch(url, data=json.dumps(data), headers=HEADERS, auth=self.cred, verify=False)
        return data

    def _post(self, request, data):
        url = 'https://' + self.device + '/api/' + request
        data = requests.post(url, data=json.dumps(data), headers=HEADERS, auth=self.cred, verify=False)
        return data

    def get_access_in(self):
        request = 'access/in'
        return self._get(request)

    def get_acl_ace(self, acl):
        request = 'objects/extendedacls/' + acl + '/aces'
        return self._get(request)

    def get_acls(self):
        request = 'objects/extendedacls'
        return self._get(request)

    def get_localusers(self):
        request = 'objects/localusers'
        return self._get(request)

    def get_networkobjectgroups(self):
        request = 'objects/networkobjectgroups'
        return self._get(request)

    def set_networkobjectgroup(self, data):
        request = 'objects/networkobjectgroups'
        return self._post(request, data)

    def replace_networkobjectgroup(self, group, data):
        request = 'objects/networkobjectgroups/' + group
        return self._patch(request, data)

