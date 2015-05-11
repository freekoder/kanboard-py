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
