# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Column(RemoteObject):
    def __init__(self, project, props):
        self.project = project
        self.id = props['id']
        self.title = props['title']
        self.position = int(props['position'])
        self.task_limit = int(props['task_limit'])
        super(Column, self).__init__(project.url, project.token)

    def __unicode__(self):
        return u'Column{#' + unicode(self.id) + u', title: ' + self.title + \
               u', position: ' + unicode(self.position) + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')