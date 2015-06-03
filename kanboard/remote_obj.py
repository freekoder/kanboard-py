# -*- coding: utf-8 -*-
__author__ = 'freekoder'

import json
import requests


class RemoteObject(object):

    _request_id = 0
    token = None
    rpc_username = 'jsonrpc'
    headers = {'content-type': 'application/json'}

    def __init__(self, url, token):
        self.url = url
        self.token = token

    def _get_request_id(self):
        self._request_id += 1
        return self._request_id

    def _create_request_params(self, methon_name, rid, params=None):
        request_params = {
            'id': rid,
            'jsonrpc': '2.0',
            'method': methon_name,
        }
        if params:
            request_params['params'] = params
        return request_params

    def _send_request_with_assert(self, params, rid):
        response = requests.post(self.url, data=json.dumps(params), headers=self.headers,
                                 auth=(self.rpc_username, self.token))
        assert response.ok
        assert response.json()['id'] == rid
        return response.json()['result']

    # TODO: handle error
    def _send_template_request(self, method_name, params=None):
        rid = self._get_request_id()
        request = self._create_request_params(method_name, rid, params)
        response = requests.post(self.url, data=json.dumps(request), headers=self.headers,
                                 auth=(self.rpc_username, self.token))
        if response.ok and response.json()['id'] == rid and ('result' in response.json()):
            return True, response.json()['result']
        else:
            return False, 'Error'