# -*- coding: utf-8 -*-
import base64

__author__ = 'freekoder'

from remote_obj import RemoteObject


class Attachment(RemoteObject):

    def __init__(self, task, props):
        self.task = task
        self.id = int(props['id'])
        self.name = props['name']
        self.path = props['path']
        self.is_image = True if props['is_image'] else False
        self.date = props['date']
        self.user = task.project.board.get_user_by_id(int(props['user_id']))
        self.size = int(props['size'])
        super(Attachment, self).__init__(task.url, task.token)

    def remove(self):
        (status, result) = self._send_template_request('removeFile', {'file_id': self.id})
        if status and result:
            return result
        else:
            return False

    def get_content(self):
        (status, result) = self._send_template_request('downloadFile', {'file_id': self.id})
        if status and result:
            return base64.decodestring(result)
        else:
            return None

    def __unicode__(self):
        return u'Attachment{name: ' + self.name + u', size:' + unicode(self.size) + u'}'

    def __str__(self):
        return unicode(self).encode('utf-8')