#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kanboard
from kanboard.subtask import Subtask


def main():
    board = kanboard.Kanboard('http://localhost:8000/jsonrpc.php',
                              'f3ef774d36cb3eee20cd5ee0c9905dfca36dae4c661546dd86c15297a2e2')

    # board.create_link('distrupt')
    #

    # link = board.get_link_by_id(14)
    # link.update('disepticon')
    # links = board.get_all_links()
    # for link in links:
    #     print str(link) + ' => ' + str(link.opposite())

    users = board.get_all_users()
    for user in users:
        print user

    project = board.get_project_by_name('Test')
    swimlanes = project.get_swimlanes()
    for swimlane in swimlanes:
        print swimlane.name

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

    # admin_user = board.get_user_by_username('simple')
    # print 'User: ' + str(admin_user)
    # print admin_user.update(email='done@test.com')
    # test_project = board.get_project_by_name('Test')
    # tasks = test_project.get_tasks()
    # for task in tasks:
    #     success = task.create_file('test.txt', False, '/tmp/test.txt')
        # files = task.get_all_files()
        # for attach in files:
        #     print attach.remove()
        #     if '.txt' in attach.name:
            #     print attach.get_content()
        # print success
        # if task.get_all_files():
        #     for attachment in task.get_all_files():
        #         print attachment
    # columns = test_project.get_columns()
    # # columns[2].move_down()
    # for column in columns:
    #     column.update(column.title, description='test description', task_limit=5)
    # task = test_project.get_tasks()[0]
    # print task
    # subtask = task.create_subtask('test subtask', user=admin_user)
    # print subtask
    #
    # for subtask in task.get_all_subtasks():
    #     subtask.update('OK OB')
    #     subtask.update_status(Subtask.STATUS_DONE)
    #     print subtask
    #     subtask.remove()
    # backlog = test_project.get_column_by_name('Work in progress')
    # done = test_project.get_column_by_name('Done')
    # print backlog
    # print done
    # for task in backlog.get_tasks():
    #     print task.move(done)

    # swimlane = test_project.get_swimlane_by_name('Default swimlane')
    # columns = swimlane.get_columns()
    # for column in columns:
    #     print column
    #     tasks = column.get_tasks()
    #     for task in tasks:
    #         print u'\t' + unicode(task)
    #
    # first_swimlane = test_project.get_swimlane_by_name('First Swimlane')
    # done_column = first_swimlane.get_column_by_name('Done')
    # done_column.create_task('test creation for swimlane')
    # backlog = test_project.get_column_by_name('Backlog')
    # tasks = backlog.get_tasks()
    # for task in tasks:
    #     print task.swimlane
    # swimlane = test_project.get_swimlane_by_name('First Swimlane')
    # test_project.create_task('test from script2', owner=admin_user, swimlane=swimlane)
    # # tasks = test_project.get_tasks()
    # # for task in tasks:
    # #     print task.swimlane
    #
    # swimlanes = test_project.get_all_swimlanes()
    # for swimlane in swimlanes:
    #     print swimlane

    # swimlane = test_project.get_swimlane_by_name('First Swimlane')
    # print swimlane
    # for category in test_project.get_all_categories():
    #     print category
    #
    # tasks = test_project.get_tasks()
    # # for task in tasks:
    # #     print task.category
    #
    # closed_tasks = test_project.get_closed_tasks()
    # for task in closed_tasks:
    #     task.open()
    #
    #
    #
    # host_category = test_project.get_category_by_name('host')
    # for task in tasks:
    #     task.update(category=host_category, color=Task.COLOR_BLUE, description='Test description')
    #     task.update(title='Hi kanboard')
    #     task.create_comment(admin_user, 'Test comment from admin')


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