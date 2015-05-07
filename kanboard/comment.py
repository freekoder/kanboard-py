# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Comment(RemoteObject):

    def __init__(self, task, props):
        self.id = int(props['id'])
        self.date = props['date']
        self.task = task
        self.user_id = props['user_id']
        # self.user = TODO: implement
        self.comment = props['comment']
        self.username = props['username']
        self.name = props['name']
        super(Comment, self).__init__(task.url, task.token)

    # TODO: implement
    def update(self, content):
        pass

    # TODO: implement
    def remove(self):
        pass

    def __unicode__(self):
        return u'Comment{#' + unicode(self.id) + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')