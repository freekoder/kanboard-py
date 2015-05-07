#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kanboard
from kanboard.task import Task


def main():
    board = kanboard.Kanboard('http://localhost:8080/jsonrpc.php',
                              '347a020cb5ce709441aa42b2d5652fbb8b02e477104d1d9789f7b2d40df0')
    # user = board.create_user('Масимо23', '123456', name='test', email='test5@email.com')
    # if user:
    #     print user
    # else:
    #     print 'Can not create user'
    project = board.get_project_by_name('Test')
    # print project
    # tasks = project.get_closed_tasks()
    # for task in tasks:
    #     print task.color
    column = project.get_column_by_name(u'Backlog')
    print column
    if column:
        tasks = column.get_tasks()
        for task in tasks:
            print task.get_all_comments()
    # user = board.create_user('test_def', '123456', default_project=project)
    # print user
    # users = board.get_all_users()
    # for user in users:
    #     print user


if __name__ == '__main__':
    main()