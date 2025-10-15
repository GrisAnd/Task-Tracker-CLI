import sys
import json
from datetime import datetime

file_path = "tasks/tasks.json"


def main():
    if len(sys.argv) < 2:
        print("Enter a valid number of arguments")

    if sys.argv[1] == "add":
        add_task()


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


if __name__ == "__main__":
    main()