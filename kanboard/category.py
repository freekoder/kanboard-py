# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Category(RemoteObject):

    # TODO: get project from props['project_id']
    def __init__(self, project, props):
        self.id = int(props['id'])
        self.name = props['name']
        self.project = project
        super(Category, self).__init__(project.url, project.token)

    # TODO: implement
    def update(self, name):
        pass

    # TODO: implement
    def remove(self):
        pass

    def __unicode__(self):
        return u'Category{#' + unicode(self.id) + u', name: ' + self.name + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')
