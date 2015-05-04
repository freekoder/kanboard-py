# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Swimlane(RemoteObject):
    def __init__(self, project, props):
        super(Swimlane, self).__init__(project.url, project.token)

    # TODO: implement
    def move_up(self):
        pass

    # TODO: implement
    def move_down(self):
        pass

    # TODO: implement
    def update(self):
        pass

    # TODO: implement
    def remove(self):
        pass

    # TODO: implement
    def enable(self, value):
        pass