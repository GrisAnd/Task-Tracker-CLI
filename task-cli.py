import sys
import json
import os
from datetime import datetime

file_path = "tasks/tasks.json"


def main():
    
    if len(sys.argv) < 2:
        print("Enter a valid number of arguments")

    if sys.argv[1] == "add":
        if os.path.exists(file_path):
            add_new_task()
        else:
            data = {
                "tasks": [
                    {
                    "id": 0,
                    "description": "",
                    "status": "",
                    "createdAt": "",
                    "updatedAt": ""
                    }
                ]
                }
            
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=2)
                
            add_new_task()
    elif sys.argv[1] == "list":
        if sys.argv[-1] == "done":
            list_done_tasks()
        elif sys.argv[-1] == "todo":
            list_todo_tasks()
        elif sys.argv[-1] == "in-progress":
            list_in_progress_tasks()
        else:
            list_all_tasks()
    elif sys.argv[1] == "update":
        update_task_description()
    elif sys.argv[1] == "mark-done" or sys.argv[1] == "mark-in-progress" or sys.argv[1] == "mark-todo":
        update_task_status()
    elif sys.argv[1] == "delete":
        delete_task()
    else:
        print("Enter a valid argument")


def add_new_task():

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


def list_all_tasks():

    with open(file_path, 'r') as file:
        data = json.load(file)

    task_number = int(data['tasks'][-1]['id'])
    i = 1

    while i <= task_number:
        print(f"ID: {data['tasks'][i]['id']}")
        print(f"Description: {data['tasks'][i]['description']}")
        print(f"Status: {data['tasks'][i]['status']}")
        print(f"Created At: {data['tasks'][i]['createdAt']}")
        print(f"Updated At: {data['tasks'][i]['updatedAt']}\n")
        i += 1


def update_task_description():

    with open(file_path, 'r') as file:
        data = json.load(file)

    task_id = int(sys.argv[2])
    updatedAt = datetime.now().strftime("%m/%d/%Y")
    max_tasks_id = int(data['tasks'][-1]['id'])

    if task_id <= max_tasks_id and task_id != 0:
        data['tasks'][task_id]['description'] = sys.argv[3]
        data['tasks'][task_id]['updatedAt'] = updatedAt

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

        print(f"Task updated successfully (ID: {task_id})")
    else: 
        print("Enter a valid task ID")


def update_task_status():
    
    with open(file_path, 'r') as file:
        data = json.load(file)

    task_id = int(sys.argv[2])
    updatedAt = datetime.now().strftime("%m/%d/%Y")
    max_tasks_id = int(data['tasks'][-1]['id'])
    status_done, status_inprogress, status_todo = "done", "in-progress", "todo"

    if task_id <= max_tasks_id and task_id != 0:
        if sys.argv[1] == "mark-done":
            data['tasks'][task_id]['status'] = status_done
            data['tasks'][task_id]['updatedAt'] = updatedAt
        elif sys.argv[1] == "mark-in-progress":
            data['tasks'][task_id]['status'] = status_inprogress
            data['tasks'][task_id]['updatedAt'] = updatedAt
        elif sys.argv[1] == "mark-todo":
            data['tasks'][task_id]['status'] = status_todo
            data['tasks'][task_id]['updatedAt'] = updatedAt

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

        print(f"Status updated successfully (ID: {task_id})")

    else:
        print("Enter a valid task ID")


def delete_task():
    
    with open(file_path, 'r') as file:
        data = json.load(file)

    task_id = int(sys.argv[2])
    max_task_id = int(data['tasks'][-1]['id'])

    if task_id <= max_task_id and task_id != 0:
        data['tasks'].pop(task_id)

        i = 1
        while i < max_task_id:
            max_task_id = int(data['tasks'][-1]['id'])
            data['tasks'][i]['id'] = data['tasks'].index(data['tasks'][i])
            i += 1

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

        print(f"Successfully deleted task (ID: {task_id})")
    else:
        print("Enter a valid task ID")


def list_done_tasks():

    with open(file_path, 'r') as file:
        data = json.load(file)

    max_task_id = data['tasks'][-1]['id']
    
    i = 1
    while i <= max_task_id:
        if data['tasks'][i]['status'] == "done":
            print(f"ID: {data['tasks'][i]['id']}")
            print(f"Description: {data['tasks'][i]['description']}")
            print(f"Status: {data['tasks'][i]['status']}")
            print(f"Created At: {data['tasks'][i]['createdAt']}")
            print(f"Updated At: {data['tasks'][i]['updatedAt']}\n")
        i += 1


def list_todo_tasks():

    with open(file_path, 'r') as file:
        data = json.load(file)

    max_task_id = data['tasks'][-1]['id']
    
    i = 1
    while i <= max_task_id:
        if data['tasks'][i]['status'] == "todo":
            print(f"ID: {data['tasks'][i]['id']}")
            print(f"Description: {data['tasks'][i]['description']}")
            print(f"Status: {data['tasks'][i]['status']}")
            print(f"Created At: {data['tasks'][i]['createdAt']}")
            print(f"Updated At: {data['tasks'][i]['updatedAt']}\n")
        i += 1

def list_in_progress_tasks():
    with open(file_path, 'r') as file:
        data = json.load(file)

    max_task_id = data['tasks'][-1]['id']
    
    i = 1
    while i <= max_task_id:
        if data['tasks'][i]['status'] == "in-progress":
            print(f"ID: {data['tasks'][i]['id']}")
            print(f"Description: {data['tasks'][i]['description']}")
            print(f"Status: {data['tasks'][i]['status']}")
            print(f"Created At: {data['tasks'][i]['createdAt']}")
            print(f"Updated At: {data['tasks'][i]['updatedAt']}\n")
        i += 1


if __name__ == "__main__":
    main()