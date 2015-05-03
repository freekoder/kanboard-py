# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class User(RemoteObject):

    def __init__(self, board, props):
        super(User, self).__init__(board.url, board.token)

    # TODO: implement
    def update(self, username=None, name=None, email=None, is_admin=None, default_project=None):
        pass

    # TODO: implement
    def remove(self):
        pass