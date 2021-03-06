Kanboard-py
===========

Kanboard python API client
It wraps internal JSON-RPC protocol with classes and simplifies client applications creation.

Dependencies
------------
- json
- requests

Tested on
---------
- python 2.7.9

Code samples
------------

Create task on specified project column
```python
import kanboard
from kanboard.task import Task

board = kanboard.Kanboard('http://localhost:8080/jsonrpc.php',
                          '347a020cb5ce709441aa42b2d5652fbb8b02e477104d1d9789f7b2d40df0')

project = board.get_project_by_name('Test')
column = project.get_column_by_name('Work in progress')
task = column.create_task('Test title', description='test descr', color=Task.COLOR_ORANGE)
```

Iterate over all project tasks
```python
import kanboard
from kanboard.task import Task

board = kanboard.Kanboard('http://localhost:8080/jsonrpc.php',
                          '347a020cb5ce709441aa42b2d5652fbb8b02e477104d1d9789f7b2d40df0')

project = board.get_project_by_name('Test')
tasks = project.get_all_tasks()
for task in tasks:
    print task.title
```

Close all tasks in column
```python
board = kanboard.Kanboard('http://localhost:8080/jsonrpc.php',
                          '347a020cb5ce709441aa42b2d5652fbb8b02e477104d1d9789f7b2d40df0')

project = board.get_project_by_name('Test')
column = project.get_column_by_name('Done')
tasks = column.get_tasks()
for task in tasks:
    task.close()
```

Show comments of red tasks in column
```python
board = kanboard.Kanboard('http://localhost:8080/jsonrpc.php',
                          '347a020cb5ce709441aa42b2d5652fbb8b02e477104d1d9789f7b2d40df0')

project = board.get_project_by_name('Test')
column = project.get_column_by_name('Work in progress')
tasks = column.get_tasks()
for task in tasks:
    if task.color == Task.COLOR_RED:
        for comment in task.get_all_comments():
            print comment.comment
```

Close all tasks at 'Done' column
```python
board = kanboard.Kanboard('http://localhost:8080/jsonrpc.php',
                          '347a020cb5ce709441aa42b2d5652fbb8b02e477104d1d9789f7b2d40df0')

project = board.get_project_by_name('Test')
column = project.get_column_by_name('Done')
tasks = column.get_tasks()
for task in tasks:
    task.close()
```

Update category and color of tasks
```python
board = kanboard.Kanboard('http://localhost:8080/jsonrpc.php',
                          '347a020cb5ce709441aa42b2d5652fbb8b02e477104d1d9789f7b2d40df0')

project = board.get_project_by_name('Test')

host_category = project.get_category_by_name('host')
for task in project.get_tasks():
    task.update(category=host_category, color=Task.COLOR_BLUE)
```

get tasks for swimlane
```python
test_project = board.get_project_by_name('Test')
swimlane = test_project.get_swimlane_by_name('Custom swimlane')
columns = swimlane.get_columns()
for column in columns:
    print column
    for task in column.get_tasks():
        print u'\t' + unicode(task)
```

create task on swimlane
```python
test_project = board.get_project_by_name('Test')
first_swimlane = test_project.get_swimlane_by_name('First Swimlane')
first_swimlane.create_task('Sample title')
```

create task on swimlane and specified column
```python
test_project = board.get_project_by_name('Test')
first_swimlane = test_project.get_swimlane_by_name('First Swimlane')
done_column = first_swimlane.get_column_by_name('Done')
done_column.create_task('test creation for swimlane')
```

create subtask
```python
test_project = board.get_project_by_name('Test')
task = test_project.get_tasks()[0]
subtask = task.create_subtask('test subtask')
```

close all subtask
```python
test_project = board.get_project_by_name('Test')
task = test_project.get_tasks()[0]
for subtask in task.get_all_subtasks():
    subtask.update_status(Subtask.STATUS_DONE)
```

add attachment to task
```python
test_project = board.get_project_by_name('Test')
task = test_project.get_tasks()[0]
task.create_file('test.txt', False, '/tmp/test.txt')
```

get all attachments
```python
test_project = board.get_project_by_name('Test')
task = test_project.get_tasks()[0]
task.get_all_files()
```

get attachment content
```python
test_project = board.get_project_by_name('Test')
task = test_project.get_tasks()[0]
attachment = task.get_all_files()[0].get_content()
```

create new link with opposite one
```python
board = kanboard.Kanboard('http://localhost:8080/jsonrpc.php',
                          '347a020cb5ce709441aa42b2d5652fbb8b02e477104d1d9789f7b2d40df0')
link = board.create_link('manage', 'managed by')
```

get link by label and show opposite link
```python
link = board.get_link_by_label('manage')
print link.opposite()
```

get all links
```python
links = board.get_all_links()
```

update link label
```python
link = board.get_link_by_id(10)
link.update('prepared before')
```
