# -*- coding: utf-8 -*-
__author__ = 'user'


class Project():

    def __init__(self, board, props):
        self.board = board
        self.id = int(props['id'])
        self.name = props['name'].encode('utf-8')
        self.is_active = True if props['is_active'] else False
        self.token = props['token']
        self.last_modified = props['last_modified']
        self.is_public = True if props['is_public'] else False
        self.description = props['description']

    def __unicode__(self):
        return u'Project{#' + unicode(self.id) + u', name: ' + self.name.decode('utf-8') + u', active: ' + \
               unicode(self.is_active) + ', public: ' + unicode(self.is_public) + '}'

    def __str__(self):
        return unicode(self).encode('utf-8')
