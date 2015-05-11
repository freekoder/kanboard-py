# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject
from column import Column
from task import Task


class Project(RemoteObject):

    def __init__(self, board, props):
        self.board = board
        self.id = int(props['id'])
        self.name = props['name']
        self.is_active = True if props['is_active'] == u'1' else False
        self.token = props['token']
        self.last_modified = props['last_modified']
        self.is_public = True if props['is_public'] == u'1' else False
        self.description = props['description']
        super(Project, self).__init__(board.url, board.token)

    def update_name(self, name):
        rid = self._get_request_id()
        params = self._create_request_params('updateProject', rid, {'id': self.id, 'name': name})
        success = self._send_request_with_assert(params, rid)
        if success:
            self.name = name
            return True
        else:
            return False

    def update_description(self, description):
        rid = self._get_request_id()
        params = self._create_request_params('updateProject', rid, {'id': self.id,
                                                                    'name': self.name,
                                                                    'description': description})
        success = self._send_request_with_assert(params, rid)
        if success:
            self.description = description
            return True
        else:
            return False

    def update_token(self, token):
        rid = self._get_request_id()
        params = self._create_request_params('updateProject', rid, {'id': self.id,
                                                                    'name': self.name,
                                                                    'token': token})
        success = self._send_request_with_assert(params, rid)
        if success:
            self.token = token
            return True
        else:
            return False

    def remove(self):
        rid = self._get_request_id()
        params = self._create_request_params('removeProject', rid, {'project_id': self.id})
        return self._send_request_with_assert(params, rid)

    def enable(self, enable):
        rid = self._get_request_id()
        params = self._create_request_params('enableProject', rid, {'project_id': self.id})
        if not enable:
            params = self._create_request_params('disableProject', rid, {'project_id': self.id})
        success = self._send_request_with_assert(params, rid)
        if success:
            self.is_active = enable
            return True
        else:
            return False

    def set_public(self, public):
        rid = self._get_request_id()
        params = self._create_request_params('enableProjectPublicAccess', rid, {'project_id': self.id})
        if not public:
            params = self._create_request_params('disableProjectPublicAccess', rid, {'project_id': self.id})
        success = self._send_request_with_assert(params, rid)
        if success:
            self.is_public = public
            return True
        else:
            return False

    # TODO: wrap activity into event class
    # TODO: handle limit, start, end params
    def get_activity(self, limit=0, start=0, end=0):
        rid = self._get_request_id()
        params = self._create_request_params('getProjectActivity', rid, {'project_ids': [self.id]})
        activity = self._send_request_with_assert(params, rid)
        return activity

    # TODO: convert id/username map to user list
    def get_members(self):
        rid = self._get_request_id()
        params = self._create_request_params('getMembers', rid, {'project_id': self.id})
        members = self._send_request_with_assert(params, rid)
        return members

    # TODO: implement
    def revoke_user(self, user):
        pass

    # TODO: implement
    def allow_user(self, user):
        pass

    # TODO: implement
    def get_board_info(self):
        pass

    def get_columns(self):
        (status, result) = self._send_template_request('getColumns', {'project_id': self.id})
        if status:
            columns = []
            for column_info in result:
                columns.append(Column(self, column_info))
            return columns
        else:
            return []

    def get_column_by_id(self, id):
        (status, result) = self._send_template_request('getColumn', {'column_id': id})
        if status:
            return Column(self, result)
        else:
            return None

    def get_column_by_name(self, name):
        if type(name) is str:
            name = name.decode('utf-8')
        columns = self.get_columns()
        for column in columns:
            if column.title == name:
                return column
        return None

    # TODO: implement
    def move_column_up(self, column):
        pass

    # TODO: implement
    def move_column_down(self, column):
        pass

    # TODO: implement
    def add_column(self, title, task_limit=0, description=''):
        pass

    # TODO: implement
    def get_swimlines(self):
        pass

    # TODO: implement, difference with get_swimlines
    def get_all_swimlines(self):
        pass

    # TODO: implement
    def get_swimline_by_id(self, id):
        return None

    # TODO: implement
    def get_swimline_by_name(self, name):
        pass

    # TODO: implement
    def add_swimline(self, name):
        pass

    # TODO: implement
    def get_available_actions(self):
        pass

    # TODO: implement
    def get_available_events(self):
        pass

    # TODO: implement
    def get_compatible_events(self):
        pass

    # TODO: implement
    def get_actions(self):
        pass

    # TODO: implement
    def create_action(self, event_name, action_name, params):
        pass

    # TODO: implement, move to action class?
    def remove_action(self, action_id):
        pass

    # TODO: implement recurrence fields
    def create_task(self, title, color='', column=None, description='',
                    owner=None, creator=None, score=0,
                    date_due=None, category=None, swimlane=None):
        params = {'title': title, 'project_id': self.id}
        if color:
            params.update({'color_id': color})
        if column:
            params.update({'column_id': column.id})
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
            return self.get_task_by_id(result)
        else:
            return None

    def get_task_by_id(self, task_id):
        (status, result) = self._send_template_request('getTask', {'task_id': task_id})
        if status and result:
            return Task(self, result)
        else:
            return None

    def get_tasks(self, status=Task.OPENED):
        (success, result) = self._send_template_request('getAllTasks', {'project_id': self.id, 'status_id': status})
        if success and result:
            tasks = []
            for task_info in result:
                tasks.append(Task(self, task_info))
            return tasks
        else:
            return []

    def get_opened_tasks(self):
        return self.get_tasks(status=Task.OPENED)

    def get_closed_tasks(self):
        return self.get_tasks(status=Task.CLOSED)

    # TODO: implement
    def get_overdue_tasks(self):
        pass

    # TODO: implement
    def create_category(self, name):
        pass

    # TODO: implement
    def get_category_by_id(self, id):
        pass

    # TODO: implement
    def get_category_by_name(self, name):
        pass

    # TODO: implement
    def get_all_categories(self):
        pass

    def __unicode__(self):
        return u'Project{#' + unicode(self.id) + u', name: ' + self.name + u', active: ' + \
               unicode(self.is_active) + u', public: ' + unicode(self.is_public) + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')
