# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Task(RemoteObject):

    def __init(self, project, props):
        self.id = props['id']
        super(Task, self).__init__(project.url, project.token)

    # TODO: implement
    def update(self, title=None, color=None, column=None, description=None,
                    owner_user=None, creator_user=None, score=None,
                    date_due=None, category=None, swimline=None):
        pass

    # TODO: implement
    def open(self):
        pass

    # TODO: implement
    def close(self):
        pass

    # TODO: implement
    def remove(self):
        pass

    # TODO: implement
    def move(self, column, position):
        pass

    # TODO: implement
    def create_comment(self, user, content):
        pass

    #TODO: implement (???)
    def get_comment(self, id):
        pass

    # TODO: implement
    def get_all_comments(self):
        pass

    # TODO: implement
    def create_subtask(self, title, user=None, time_estimated=None, time_spent=None, status=None):
        pass

    # TODO: implement
    def get_subtask_by_id(self, id):
        pass

    # TODO: implement
    def get_all_subtasks(self):
        pass
