# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Category(RemoteObject):

    def __init__(self, project, props):
        super(Category, self).__init__(project.url, project.token)

    # TODO: implement
    def update(self, name):
        pass

    # TODO: implement
    def remove(self):
        pass
