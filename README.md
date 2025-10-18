# README
Simple Task tracker project, based in CLI (Command Line Interface)

## Add:
python3 task-cli.py add "**task description**"

Create a new task, if the json file doesn't exists it create one.

## Update:
python3 task-cli.py update **task_id** "new task description"

Edit the task description.

## List:
python3 task-cli.py list

List all the tasks in the json file.

### List done:
python3 task-cli.py list done

List all done tasks in the json file.

### List todo:
python3 task-cli.py list todo

List all todo tasks in the json file.

### List in-progress:
python3 task-cli.py list in-progress

List all in-progress in the json file.

## Mark done:
python3 task-cli.py mark-done **task_id**

Mark the selected task as done

## Mark in-progress:
python3 task-cli.py mark-in-progress **task_id**

Mark the selected task as in-progress

## Mark todo:
python3 task-cli.py mark-todo **task_id**

Mark the selected task as todo

## Delete:
python3 task-cli.py delete **task_id**

Delete the selected task
