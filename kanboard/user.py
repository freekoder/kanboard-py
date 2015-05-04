# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject
from column import Column
from task import Task


class User(RemoteObject):
    def __init__(self, board, props):
        super(User, self).__init__(board.url, board.token)