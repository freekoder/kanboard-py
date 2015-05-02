# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Project(RemoteObject):

    def __init__(self, board, props):
        self.board = board
        self.id = int(props['id'])
        self.name = props['name'].encode('utf-8')
        self.is_active = True if props['is_active'] else False
        self.token = props['token']
        self.last_modified = props['last_modified']
        self.is_public = True if props['is_public'] else False
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

    # BUG: no update without name param
    def update_active(self, active):
        rid = self._get_request_id()
        activ_val = u'1' if active else u'0'
        params = self._create_request_params('updateProject', rid, {'id': self.id,
                                                                    'name': self.name,
                                                                    'is_active': activ_val})
        success = self._send_request_with_assert(params, rid)
        if success:
            self.is_active = active
            return True
        else:
            return False

    # BUG: no update without name param
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

    # BUG: no update without name param
    def update_public(self, public):
        rid = self._get_request_id()
        public_val = u'1' if public else u'0'
        params = self._create_request_params('updateProject', rid, {'id': self.id,
                                                                    'name': self.name,
                                                                    'is_public': public_val})
        success = self._send_request_with_assert(params, rid)
        if success:
            self.is_public = public
            return True
        else:
            return False

        # BUG: no update without name param
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


    def __unicode__(self):
        return u'Project{#' + unicode(self.id) + u', name: ' + self.name.decode('utf-8') + u', active: ' + \
               unicode(self.is_active) + ', public: ' + unicode(self.is_public) + '}'

    def __str__(self):
        return unicode(self).encode('utf-8')
