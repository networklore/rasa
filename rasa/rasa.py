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

    def __init__(self, device=None, username=None, password=None, verify_cert=True, timeout=5):
        
        self.device = device
        self.username = username
        self.password = password
        self.verify_cert = verify_cert
        self.timeout = timeout
        self.cred = HTTPBasicAuth(self.username, self.password)

    def _delete(self, request):
        url = 'https://' + self.device + '/api/' + request
        data = requests.delete(url,headers=HEADERS,auth=self.cred, verify=self.verify_cert, timeout=self.timeout)
        return data

    def _get(self, request):
        url = 'https://' + self.device + '/api/' + request
        data = requests.get(url,headers=HEADERS,auth=self.cred, verify=self.verify_cert, timeout=self.timeout)
        return data

    def _patch(self, request, data):
        url = 'https://' + self.device + '/api/' + request
        data = requests.patch(url, data=json.dumps(data), headers=HEADERS, auth=self.cred, verify=self.verify_cert, timeout=self.timeout)
        return data

    def _post(self, request, data=False):
        url = 'https://' + self.device + '/api/' + request
        if data != False:
            data = requests.post(url, data=json.dumps(data), headers=HEADERS, auth=self.cred, verify=self.verify_cert, timeout=self.timeout)
        else:
            data = requests.post(url, headers=HEADERS, auth=self.cred, verify=self.verify_cert, timeout=self.timeout)            
        return data

    def _put(self, request, data):
        url = 'https://' + self.device + '/api/' + request
        data = requests.put(url, data=json.dumps(data), headers=HEADERS, auth=self.cred, verify=self.verify_cert, timeout=self.timeout)
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

    # Network objects

    def delete_networkobject(self, net_object):
        request = 'objects/networkobjects/' + net_object
        return self._delete(request)

    def get_networkobject(self, net_object):
        request = 'objects/networkobjects/' + net_object
        return self._get(request)

    def get_networkobjects(self):
        request = 'objects/networkobjects'
        return self._get(request)

    def replace_networkobject(self, name, data):
        request = 'objects/networkobjects/' + name
        return self._put(request, data)

    def set_networkobject(self, data):
        request = 'objects/networkobjects'
        return self._post(request, data)

    # Network object-groups
    def get_networkobjectgroups(self):
        request = 'objects/networkobjectgroups'
        return self._get(request)

    def set_networkobjectgroup(self, data):
        request = 'objects/networkobjectgroups'
        return self._post(request, data)

    def replace_networkobjectgroup(self, group, data):
        request = 'objects/networkobjectgroups/' + group
        return self._patch(request, data)

    def write_mem(self):
        request = '/api/commands/writemem'
        return self._post(request)

