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

    def create_task(self, title, color='', description='',
                    owner=None, creator=None, score=0,
                    date_due=None, category=None, swimlane=None):
        params = {'title': title, 'project_id': self.project.id, 'column_id': self.id}
        if color:
            params.update({'color_id': color})
        if owner:
            params.update({'owner_id': owner.id})
        if creator:
            params.update({'creator_id': creator.id})
        if score:
            params.update({'score': score})
        if description:
            params.update({'description': description})
        if date_due:
            params.update({'date_due': date_due})
        if category:
            params.update({'category_id': category.id})
        if swimlane:
            params.update({'swimlane_id': swimlane.id})
        (status, result) = self._send_template_request('createTask', params)
        if status and result:
            return self.project.get_task_by_id(result)
        else:
            return None

    def __unicode__(self):
        return u'Column{#' + unicode(self.id) + u', title: ' + self.title + \
               u', position: ' + unicode(self.position) + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')