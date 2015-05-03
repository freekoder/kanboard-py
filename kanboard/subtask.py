# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Subtask(RemoteObject):

    def __init__(self, project, props):
        super(Subtask, self).__init__(project.url, project.token)

    # TODO: implement
    def update(self, title=None, user=None, time_estimated=None, time_spent=None, status=None):
        pass

    # TODO: implement
    def remove(self):
        pass