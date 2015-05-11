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

project = board.get_project_by_name('Test')
column = project.get_column_by_name('Work in progress')
task = column.create_task('Create from column', description='created with script', color=Task.COLOR_ORANGE)
```

Iterate over all project tasks
```python
```python
import kanboard
from kanboard.task import Task

project = board.get_project_by_name('Test')
tasks = project.get_all_tasks()
for task in tasks:
    print task.title
```