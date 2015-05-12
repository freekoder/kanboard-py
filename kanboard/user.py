# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class User(RemoteObject):
    def __init__(self, board, props):
        self.id = int(props['id'])
        self.username = props['username']
        self.password = props['password'] if 'password' in props else ''
        self.is_admin = True if props['is_admin'] == '1' else False
        self.default_project = board.get_project_by_id(int(props['default_project_id']))
        self.is_ldap_user = True if props['is_ldap_user'] == '1' else False
        self.name = props['name']
        self.email = props['email']
        self.google_id = props['google_id']
        self.github_id = props['github_id']
        self.notifications_enabled = True if props['notifications_enabled'] == '1' else False
        super(User, self).__init__(board.url, board.token)

    def __unicode__(self):
        return u'User{#' + str(self.id) + u', username: ' + self.username + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')