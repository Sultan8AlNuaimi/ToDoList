import os

TASKS_FILE = "tasks.txt"

def load_tasks(): # to load the tasks
    if not os.path.exists(TASKS_FILE):
        return[]

    with open(TASKS_FILE, "r") as f:
        tasks = f.read().splitlines()
        return tasks

def save_tasks (tasks):
    with open(TASKS_FILE,"w") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks (tasks):
    print("\nyour tasks:")
    if not tasks:
        print ("No tasks!")
        return
    for i, task in enumerate (tasks,1):
        print (f" {i}. {task}")

def add_task (tasks):
    task = input ("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(" Task added!\n")


def delete_task (tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try: 
        number = int(input("Enter the task number to delete:"))
        if 1<= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f" deleted: {removed}\n")
        else:
            print("invalid number")
    except ValueError:
        print("Please enter a valid number")

def menu():
    tasks = load_tasks()

    while True:
        print("\n ----> To Do List Menu <----")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("GoodBye! ")
            break
        else:
            print("Invalid input!")

if __name__ == "__main__":
    menu()