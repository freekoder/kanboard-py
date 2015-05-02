#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kanboard


def main():
    board = kanboard.Kanboard('http://localhost:8080/jsonrpc.php',
                              'd9269bcdeec16bc4c937b29697cb2fa9b3516f0c365537b7fd52e988b9ca')
    print 'Version: ' + board.get_version()
    print 'Timezone: ' + board.get_timezone()
    projects = board.get_all_projects()
    for project in projects:
        # project.update_description('TEST DESCRIPTION')
        # project.update_public(True)
        project.update_token('testwwierjwpeorjwpeo')
        print project

if __name__ == '__main__':
    main()