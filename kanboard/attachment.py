# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Attachment(RemoteObject):

    # TODO: implement user by id
    def __init__(self, task, props):
        self.task = task
        self.id = int(props['id'])
        self.name = props['name']
        self.path = props['path']
        self.is_image = True if props['is_image'] else False
        self.date = props['date']
        self.user = None
        self.size = int(props['size'])
        super(Attachment, self).__init__(task.url, task.token)

    def remove(self):
        pass

    def download(self, path):
        pass

    def __unicode__(self):
        return u'Attachment{name: ' + self.name + u', size:' + unicode(self.size) + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')