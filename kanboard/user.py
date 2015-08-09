# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class User(RemoteObject):
    def __init__(self, board, props):
        self.id = int(props['id'])
        self.username = props['username']
        self.password = props['password'] if 'password' in props else ''
        self.is_admin = True if props['is_admin'] == '1' else False
        self.is_ldap_user = True if props['is_ldap_user'] == '1' else False
        self.name = props['name']
        self.email = props['email']
        self.google_id = props['google_id']
        self.github_id = props['github_id']
        self.notifications_enabled = True if props['notifications_enabled'] == '1' else False
        super(User, self).__init__(board.url, board.token)

    def update(self, username=None, name=None, email=None, is_admin=None, default_project=None):
        props = {'id': self.id}
        if username:
            props['username'] = username
        if name:
            props['name'] = name
        if email:
            props['email'] = email
        if isinstance(is_admin, bool):
            props['is_admin'] = '1' if is_admin else '0'
        if default_project:
            props['default_project_id'] = default_project.id
        (status, result) = self._send_template_request('updateUser', props)
        if status and result:
            return result
        else:
            return False

    def remove(self):
        (status, result) = self._send_template_request('removeUser', {'user_id': self.id})
        if status and result:
            return result
        else:
            return False

    def __unicode__(self):
        return u'User{#' + str(self.id) + u', username: ' + self.username + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')