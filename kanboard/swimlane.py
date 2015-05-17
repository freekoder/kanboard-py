# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Swimlane(RemoteObject):

    def __init__(self, project, props):
        self.id = int(props['id'])
        self.name = props['name']
        self.is_active = True
        if 'is_active' in props:
            self.is_active = True if props['is_active'] == '1' else False
        if 'position' in props:
            self.position = int(props['position'])
        self.project = project
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

    def get_columns(self):
        wrappers = []
        columns = self.project.get_columns()
        for column in columns:
            wrappers.append(ColumnWrapper(self, column))
        return wrappers

    def get_column_by_id(self, id):
        column = self.project.get_column_by_id(id)
        return ColumnWrapper(self, column)

    def get_column_by_name(self, name):
        column = self.project.get_column_by_name(name)
        return ColumnWrapper(self, column)

    def create_task(self, title, color='', column=None, description='',
                    owner=None, creator=None, score=0,
                    date_due=None, category=None):
        return self.project.create_task(title, color, column, description,
                    owner, creator, score,
                    date_due, category, swimlane=self)

    def __unicode__(self):
        return u'Swimlane{#' + unicode(self.id) + u', name: ' + self.name + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')


class ColumnWrapper:

    def __init__(self, swimlane, column):
        self.swimlane = swimlane
        self.column = column

    def get_tasks(self):
        tasks = []
        for task in self.column.get_tasks():
            if task.swimlane.id == self.swimlane.id:
                tasks.append(task)
        return tasks

    def create_task(self, title, color='', description='',
                    owner=None, creator=None, score=0,
                    date_due=None, category=None):
        return self.column.create_task(title, color, description, owner, creator,
                                       score, date_due, category, swimlane=self.swimlane)

    def __unicode__(self):
        return u'Swimlane' + unicode(self.column)

    def __str__(self):
        return 'Swimlane' + str(self.column)
