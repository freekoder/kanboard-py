# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


def status_to_text(status):
    if status == Subtask.STATUS_OPENED:
        return 'OPENED'
    elif status == Subtask.STATUS_PROGRESS:
        return 'PROGRESS'
    elif status == Subtask.STATUS_DONE:
        return 'DONE'


class Subtask(RemoteObject):

    STATUS_OPENED = 0
    STATUS_PROGRESS = 1
    STATUS_DONE = 2

    def __init__(self, task, props):
        self.task = task
        self.id = int(props['id'])
        self.title = props['title']
        self.status = int(props['status'])
        self.time_estimated = props['time_estimated']
        self.time_spent = props['time_spent']
        self.user = task.project.board.get_user_by_id(int(props['user_id'])) if props['user_id'] else None
        super(Subtask, self).__init__(task.url, task.token)

    def update(self, title=None, user=None, time_estimated=None, time_spent=None, subtask_status=None):
        props = {'id': self.id, 'task_id': self.task.id}
        if title:
            props['title'] = title
        if user:
            props['user_id'] = user.id
        if time_estimated:
            props['time_estimated'] = time_estimated
        if time_spent:
            props['time_spent'] = time_spent
        if subtask_status:
            props['status'] = subtask_status
        (status, result) = self._send_template_request('updateSubtask', props)
        if status and result:
            if title:
                self.title = title
            if user:
                self.user = user
            if time_estimated:
                self.time_estimated = time_estimated
            if time_spent:
                self.time_spent = time_spent
            if subtask_status:
                self.status = subtask_status
            return result
        else:
            return False

    def update_status(self, subtask_status):
        return self.update(subtask_status=subtask_status)

    def remove(self):
        (status, result) = self._send_template_request('removeSubtask', {'subtask_id': self.id})
        if status and result:
            return result
        else:
            return False

    def status_to_text(self):
        return unicode(self.status)

    def __unicode__(self):
        return u'Subtask{#' + unicode(self.id) + u', title: ' + self.title + u', status: ' + status_to_text(self.status) + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')