import sys
import json
from datetime import datetime

file_path = "tasks/tasks.json"


def main():
    if len(sys.argv) < 2:
        print("Enter a valid number of arguments")

    if sys.argv[1] == "add":
        add_task()
    elif sys.argv[1] == "list":
        list_tasks()
    else:
        print("Enter a valid argument")


def add_task():

    with open(file_path, 'r') as file:
        data = json.load(file)

    task_id = data['tasks'][-1]['id'] + 1
    createdAt = datetime.now().strftime("%m/%d/%Y")
    updatedAt = createdAt

    task = [
        {
        "id": task_id,
        "description": sys.argv[2],
        "status": "todo",
        "createdAt": createdAt,
        "updatedAt": updatedAt
        }
    ]

    data['tasks'] += task

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

    print(f"Task added successfully (ID: {task_id})")


def list_tasks():
    with open(file_path, 'r') as file:
        data = json.load(file)

    task_number = int(data['tasks'][-1]['id'])
    i = 1
    while i <= task_number:
        print(data['tasks'][i])
        i += 1

if __name__ == "__main__":
    main()