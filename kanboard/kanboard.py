# -*- coding: utf-8 -*-

__author__ = 'user'

import json
import requests

import project


class Kanboard:

    _request_id = 0
    headers = {'content-type': 'application/json'}
    username = 'jsonrpc'
    token = None

    def __init__(self, url, token):
        if not url or not token:
            raise
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
                                 auth=(self.username, self.token))
        assert response.ok
        assert response.json()['id'] == rid
        return response.json()['result']

    def get_version(self):
        rid = self._get_request_id()
        params = self._create_request_params('getVersion', rid)
        return self._send_request_with_assert(params, rid)

    def get_timezone(self):
        rid = self._get_request_id()
        params = self._create_request_params('getTimezone', rid)
        return self._send_request_with_assert(params, rid)

    def create_project(self, project_name, description=''):
        if type(project_name) is str:
            project_name = project_name.decode('utf-8')
        if type(description) is str:
            description = description.decode('utf-8')
        rid = self._get_request_id()
        params = self._create_request_params('createProject', rid, {'name': project_name, 'description': description})
        project_id = self._send_request_with_assert(params, rid)
        if project_id:
            print project_id
            return self.get_project_by_id(project_id)
        else:
            print 'Can not create project with name ' + '"' + project_name + '"'
            return None

    def get_project_by_id(self, id):
        rid = self._get_request_id()
        params = self._create_request_params('getProjectById', rid, {'project_id': id})
        project_props = self._send_request_with_assert(params, rid)
        if project_props:
            return project.Project(self, project_props)
        else:
            print 'No project with id: ' + id
            return None

    def get_project_by_name(self, name):
        rid = self._get_request_id()
        if type(name) is str:
            name = name.decode('utf-8')
        params = self._create_request_params('getProjectByName', rid, {'name': name})
        project_props = self._send_request_with_assert(params, rid)
        if project_props:
            return project.Project(self, project_props)
        else:
            print 'No project with id: ' + id
            return None

    def get_all_projects(self):
        rid = self._get_request_id()
        params = self._create_request_params('getAllProjects', rid)
        projects_props = self._send_request_with_assert(params, rid)
        projects = []
        if projects_props:
            for prop in projects_props:
                projects.append(project.Project(self, prop))
        return projects
