# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from comment import Comment
from remote_obj import RemoteObject


class Task(RemoteObject):

    OPENED = 1
    CLOSED = 0

    COLOR_YELLOW = 'yellow'
    COLOR_BLUE = 'blue'
    COLOR_RED = 'red'
    COLOR_GREEN = 'green'
    COLOR_PURPLE = 'purple'
    COLOR_ORANGE = 'orange'
    COLOR_GRAY = 'gray'

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
        self.swimlane = project.get_swimline_by_id(int(props['swimlane_id']))
        self.date_completed = props['date_completed']
        self.reference = props['reference']
        self.date_modification = props['date_modification']
        self.date_started = props['date_started']
        self.time_spent = props['time_spent']
        self.time_estimated = props['time_estimated']
        self.date_moved = props['date_moved']
        self.recurrence_status = props['recurrence_status'] if 'recurrence_status' in props else None
        self.recurrence_trigger = props['recurrence_trigger'] if 'recurrence_trigger' in props else None
        self.recurrence_factor = props['recurrence_factor'] if 'recurrence_factor' in props else None
        self.recurrence_timeframe = props['recurrence_timeframe'] if 'recurrence_timeframe' in props else None
        self.recurrence_basedate = props['recurrence_basedate'] if 'recurrence_basedate' in props else None
        self.recurrence_parent = props['recurrence_parent'] if 'recurrence_parent' in props else None
        self.recurrence_child = props['recurrence_child'] if 'recurrence_child' in props else None

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

    def get_all_comments(self):
        (status, result) = self._send_template_request('getAllComments', {'task_id': self.id})
        if status and result:
            comments = []
            for comment_info in result:
                comments.append(Comment(self, comment_info))
            return comments
        else:
            return []

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
        return unicode(self).encode('utf-8')
