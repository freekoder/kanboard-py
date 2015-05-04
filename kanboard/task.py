# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Task(RemoteObject):

    OPEN = 1
    CLOSED = 0

    def __init__(self, project, props):
        self.project = project
        self.id = int(props['id'])
        self.title = props['title']
        self.description = props['description']
        self.date_creation = props['date_creation']
        self.color = props['color_id']
        self.column = project.get_column_by_id(int(props['column_id']))
        self.owner = project.board.get_user_by_id(int(props['owner_id']))
        self.position = int(props['position'])
        self.is_active = True if props['is_active'] == '1' else False
        self.date_completed = props['date_completed']
        self.score = props['score']
        self.date_due = props['date_due']
        self.category = project.get_category_by_id(int(props['category_id']))
        self.creator = project.board.get_user_by_id(int(props['creator_id']))
        self.date_modification = props['date_modification']
        self.swimline = project.get_swimline_by_id(int(props['swimline_id']))
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

    def __unicode__(self):
        return u'Task{#' + unicode(self.id) + u', title: ' + self.title + \
               u', active: ' + unicode(self.is_active) + u'}'

    def __str__(self):
        return unicode(self).decode('utf-8')
