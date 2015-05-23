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

    ######################################################################
    # General Functions
    ######################################################################
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

    ######################################################################
    # Unsorted functions
    ######################################################################
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

    ######################################################################
    # <OBJECTS>
    ######################################################################
    # Functions related to network objects, or "object network" in the
    # ASA configuration
    ######################################################################
    def create_networkobject(self, data):
        request = 'objects/networkobjects'
        return self._post(request, data)

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

    ######################################################################
    # Functions related to network object-groups, or
    # "object-group network" in the ASA configuration
    ######################################################################

    def add_member_networkobjectgroup(self, net_object, member_data):
        request = 'objects/networkobjectgroups/' + net_object
        data = {}
        data['members.add'] = member_data
        return self._patch(request, data)

    def create_networkobjectgroup(self, data):
        request = 'objects/networkobjectgroups'
        return self._post(request, data)

    def delete_networkobjectgroup(self, net_object):
        request = 'objects/networkobjectgroups/' + net_object
        return self._delete(request)

    def get_networkobjectgroup(self, net_object):
        request = 'objects/networkobjectgroups/' + net_object
        return self._get(request)

    def get_networkobjectgroups(self):
        request = 'objects/networkobjectgroups'
        return self._get(request)

    def remove_member_networkobjectgroup(self, net_object, member_data):
        request = 'objects/networkobjectgroups/' + net_object
        data = {}
        data['members.remove'] = member_data
        return self._patch(request, data)

    def replace_networkobjectgroup(self, group, data):
        request = 'objects/networkobjectgroups/' + group
        return self._patch(request, data)
    ######################################################################
    # </OBJECTS>
    ######################################################################


    ######################################################################
    # Functions related to specific commands
    ######################################################################
    def write_mem(self):
        request = 'commands/writemem'
        return self._post(request)

