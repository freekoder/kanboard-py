# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Category(RemoteObject):

    def __init__(self, project, props):
        self.id = int(props['id'])
        self.name = props['name']
        self.project = project
        super(Category, self).__init__(project.url, project.token)

    def update(self, name):
        (status, result) = self._send_template_request('updateCategory', {'id': self.id, 'name': name})
        if status and result:
            return result
        else:
            return False

    def remove(self):
        (status, result) = self._send_template_request('removeCategory', {'category_id': self.id})
        if status and result:
            return result
        else:
            return False

    def __unicode__(self):
        return u'Category{#' + unicode(self.id) + u', name: ' + self.name + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')
