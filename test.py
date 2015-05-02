#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kanboard


def main():
    board = kanboard.Kanboard('http://localhost:8080/jsonrpc.php',
                              'd9269bcdeec16bc4c937b29697cb2fa9b3516f0c365537b7fd52e988b9ca')
    print 'Version: ' + board.get_version()
    print 'Timezone: ' + board.get_timezone()
    project = board.get_project_by_name('test2_12_12')
    if project:
        column = project.get_column_by_name('Ожидающие')
        print column

if __name__ == '__main__':
    main()