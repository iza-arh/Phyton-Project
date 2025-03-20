import requests
import numpy as np
import csv

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



def generate_priority():
    return np.random.randint(1, 5) 


def get_random_quote():
    response = requests.get("https://catfact.ninja/fact")
    quote = response.json().get("fact")
    return quote



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
   



def search_task(title):
    for task in tasklist:
          if(task.title == title):
            print_task_details(task)
            return task      
    print("The task isnt in the the task list")



def delete_task(title):
    try :
      task_index = tasklist.index(search_task(title))
      tasklist.pop(task_index)
      print("the task was deleted")
    except ValueError:
      print("The task isnt in the the task list")




def taskManager():
    use_task_manager  = "yes"

    while use_task_manager == "yes":
      
      use_task_manager = input("Do you need to use the task manager?")
      type_of_function = input("What are ya gonna do?")

      if(type_of_function == "add task"):
          add_task()
      elif(type_of_function == "show task"):
          show_tasks()
      elif(type_of_function == "search a task"):
          title = input("Whats the  name of the task?")
          search_task(title)
      elif(type_of_function == "delete a task"):
          title = input("Whats the  name of the task?")
          delete_task(title)



taskManager()









