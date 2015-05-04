# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Column(RemoteObject):
    def __init__(self, project, props):
        self.project = project
        self.id = int(props['id'])
        self.title = props['title']
        self.position = int(props['position'])
        self.task_limit = int(props['task_limit'])
        super(Column, self).__init__(project.url, project.token)

    # TODO: implement
    def update(self, title, task_limit=0, description=''):
        pass

    # TODO: implement
    def remove(self):
        pass

    def get_tasks(self):
        all_tasks = self.project.get_opened_tasks()
        tasks = []
        for task in all_tasks:
            if task.column.id == self.id:
                tasks.append(task)
        return tasks

    def __unicode__(self):
        return u'Column{#' + unicode(self.id) + u', title: ' + self.title + \
               u', position: ' + unicode(self.position) + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')