# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Comment(RemoteObject):

    def __init__(self, task, props):
        super(Comment, self).__init__(task.url, task.token)

    # TODO: implement
    def update(self, content):
        pass

    # TODO: implement
    def remove(self):
        pass