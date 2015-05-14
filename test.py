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
    # users = board.get_all_users()
    # for user in users:
    #     print user
    #     print 'Email: ' + str(user.email)
    #     print 'Admin: ' + str(user.is_admin)
    #     print 'Def Project: ' + str(user.default_project)

    test_project = board.get_project_by_name('Test')
    for category in test_project.get_all_categories():
        print category

    tasks = test_project.get_tasks()
    # for task in tasks:
    #     print task.category

    closed_tasks = test_project.get_closed_tasks()
    for task in closed_tasks:
        task.open()

    host_category = test_project.get_category_by_name('host')
    for task in tasks:
        task.update(category=host_category, color=Task.COLOR_BLUE, description='Test description')
        task.update(title='Hi kanboard')


    # done_task = test_project.get_column_by_name('Done').get_tasks()
    # for task in done_task:
    #     task.remove()

    # project = board.get_project_by_name('Test')
    # column = project.get_column_by_name('Done')
    # tasks = column.get_tasks()
    # for task in tasks:
    #     task.close()
    # task = column.create_task('Create from column', description='created with script', color=Task.COLOR_ORANGE)


    # task = project.create_task('Created task', description='Test description', color=Task.COLOR_GREEN, column=column)
    # print task
    # print project
    # tasks = project.get_closed_tasks()
    # for task in tasks:
    #     print task.color
    # column = project.get_column_by_name(u'Backlog')
    # print column
    # if column:
    #     tasks = column.get_tasks()
    #     for task in tasks:
    #         print task.get_all_comments()
    # user = board.create_user('test_def', '123456', default_project=project)
    # print user
    # users = board.get_all_users()
    # for user in users:
    #     print user


if __name__ == '__main__':
    main()