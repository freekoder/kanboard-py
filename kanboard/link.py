# -*- coding: utf-8 -*-
__author__ = 'freekoder'

from remote_obj import RemoteObject


class Link(RemoteObject):

    def __init__(self, board, props):
        self.board = board
        self.id = int(props['id'])
        self.label = props['label']
        self.opposite_id = props['opposite_id']
        super(Link, self).__init__(board.url, board.token)

    def opposite(self):
        return self.board.get_link_by_id(self.opposite_id)

    def update(self, label):
        (status, result) = self._send_template_request('updateLink', {'link_id': self.id,
                                                                      'opposite_link_id': self.opposite_id,
                                                                      'label': label})
        if status and result:
            self.label = label
            return True
        else:
            return False

    def remove(self):
        (status, result) = self._send_template_request('removeLink', {'link_id': self.id})
        if status and result:
            return True
        else:
            return False

    def __unicode__(self):
        return u'Link{#' + unicode(self.id) + u', label: ' + self.label + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')