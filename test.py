import requests
import numpy as np
import csv
import os

tasklistFields = ["title", "description", "status", "priority", "quote"]
tasklist = []
tasklist_filename = "tasklist_file.csv"

class Task:
    def __init__(self, title, description, status, priority, quote):
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.quote = quote


def write_tasks(task):
    file_exists = os.path.exists('data.csv')
    
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, tasklistFields)
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(task.__dict__)

def read_tasks_from_csv():
    with open('data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for task in reader:
           new_task = Task(task[0], task[1], task[2], task[3], task[4])
           tasklist.append(new_task)


def generate_priority():
    return np.random.randint(1, 5) 


def get_random_quote():
    response = requests.get("https://catfact.ninja/fact")
    quote = response.json().get("fact")
    return quote

def uppercase_task_status(function):
    def wrapper():
        task_obj = function()
        task_obj.status = task_obj.status.upper()
        print(task_obj.status)
        return task_obj
    return wrapper

@uppercase_task_status
def create_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    status = input("Enter task status: ")
    priority = generate_priority()
    quote = get_random_quote()
    taskN = Task(title, description, status, priority, quote)
    return taskN


def add_task():
    insertTask = "yes"

    while insertTask == "yes":
      tasklist.append(create_task())
      insertTask = input ("Do you want to add another new task?")



def print_task_details(task):
    print("title: " + task.title)
    print("description: " + task.description)
    print("status: " + task.status)
    print(f"priority: {task.priority}")
    print("cat fact: " + task.quote)
    print("")



def show_tasks():
    for task in tasklist:
        print_task_details(task)
   

high_priority_tasks = [x for x in tasklist if x.priority == "5"]
for task in high_priority_tasks:
    print_task_details(task)

def search_task(title):
    for task in tasklist:
          if(task.title == title):
            print_task_details(task)
            return task      
    print("The task isnt in the the task list")

def log_deletions(fichero_log_name):
    def decorator_log(function):
        def decorator_function(title):
            task_obj = function(title)
            with open(fichero_log_name, mode='a') as opened_file:
                opened_file.write(str(task_obj.__dict__) + "\n")
        return decorator_function
    return decorator_log

@log_deletions("deletions.log")
def delete_task(title):
    try :
      task_index = tasklist.index(search_task(title))
      deleted_task = tasklist[task_index]
      tasklist.pop(task_index)
      print("the task was deleted")
      return deleted_task
    except ValueError:
      print("The task isnt in the the task list")


def find_task_based_on_priority(priority):
    for task in tasklist:
            if(task.priority == priority):
                print_task_details(task)

def sort_tasks():
    sorted_tasks = sorted(tasklist, key=lambda x: x.priority)  
    print("\nSorted Tasks by Priority:")
    for task in sorted_tasks:
        print_task_details(task)

def task_manager():
    use_task_manager = input("Do you need to use the task manager?")
    while use_task_manager == "yes":

      print("\n1. Add Task")
      print("2. Show Tasks")
      print("3. Search Task")
      print("4. Delete Tasks")
      print("5. Find task based on priority")
      print("6. Sort tasks based on priority")

      choice = int(input("Choose an option: "))

      if(choice == 1):
          add_task()
      elif(choice == 2):
          show_tasks()
      elif(choice == 3):
          title = input("Whats the  name of the task?")
          search_task(title)
      elif(choice == 4):
          title = input("Whats the  name of the task?")
          delete_task(title)
      elif(choice == 5):
          priority_number = int(input("Insert the number of priority "))
          find_task_based_on_priority(priority_number)
      elif(choice == 6):
          sort_tasks()
      use_task_manager = input("Do you need to use the task manager?")













