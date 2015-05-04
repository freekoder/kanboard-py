# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from user import User
from column import Column
from remote_obj import RemoteObject
import project


class Kanboard(RemoteObject):

    def __init__(self, url, token):
        super(Kanboard, self).__init__(url, token)

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

    def get_project_by_id(self, project_id):
        rid = self._get_request_id()
        params = self._create_request_params('getProjectById', rid, {'project_id': project_id})
        project_props = self._send_request_with_assert(params, rid)
        if project_props:
            return project.Project(self, project_props)
        else:
            print 'No project with id: ' + str(project_id)
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
            print 'No project with name: ' + name
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

    # TODO: think about method remove from kanboard class
    def get_column_by_id(self, id):
        (status, result) = self._send_template_request('getColumn', {'column_id': id})
        if status and result:
            return Column(self, result)
        else:
            return None

    # TODO: implement (think about method remove from kanboard class)
    def get_task_by_id(self, task_id):
        pass

    def create_user(self, username, password, name=None, email=None, is_admin=None, default_project=None):
        props = {'username': username, 'password': password}
        if name:
            props['name'] = name if type(name) is unicode else name.decode('utf-8')
        if email:
            props['email'] = email
        if is_admin:
            props['is_admin'] = 1 if is_admin else 0
        if default_project:
            props['default_project_id'] = default_project.id
        (status, result) = self._send_template_request('createUser', props)
        if status and result:
            return self.get_user_by_id(result)
        else:
            return None

    # TODO: implement
    def create_ldap_user(self, username=None, email=None, is_admin=None, default_project=None):
        pass

    def get_user_by_id(self, user_id):
        (status, result) = self._send_template_request('getUser', {'user_id': user_id})
        if status and result:
            return User(self, result)
        else:
            return None

    def get_all_users(self):
        (status, result) = self._send_template_request('getAllUsers')
        if status and result:
            users = []
            for user_info in result:
                users.append(User(self, user_info))
            return users
        else:
            return []

    # TODO: implement
    def get_overdue_tasks(self):
        pass