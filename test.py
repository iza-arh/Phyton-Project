import requests
import numpy as np
import csv

tasklistFields = ["title", "description", "status", "priority", "quote"]
tasklist = []
tasklist_filename = "tasklist_file.csv"

with open('data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile) 
    
    for row in reader:
        print(row)

        
class Task:
    def __init__(self, title, description, status, priority, quote):
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.quote = quote


# Instantiations to test
task1 = Task(
    title="Finish Report",
    description="Complete the monthly financial report.",
    status="In Progress",
    priority=3,
    quote="Time is money."
)

task2 = Task(
    title="Team Meeting",
    description="Weekly team sync-up to discuss project updates.",
    status="Pending",
    priority=4,
    quote="Collaboration brings success."
)

task3 = Task(
    title="Code Review",
    description="Review the pull request for the new feature.",
    status="Completed",
    priority=5,
    quote="Quality is not an act, it's a habit."
)

task4 = Task(
    title="Write Documentation",
    description="Document the newly implemented functions and modules.",
    status="Pending",
    priority=2,
    quote="Good documentation is key to success."
)

task5 = Task(
    title="Bug Fix",
    description="Fix the issue causing the application to crash on startup.",
    status="In Progress",
    priority=1,
    quote="Fix the bugs, improve the product."
)

tasklist.append(task1)
tasklist.append(task2)
tasklist.append(task3)
tasklist.append(task4)
tasklist.append(task5)

with open('data.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, tasklistFields)
    writer.writeheader()
    for task in tasklist:
        writer.writerow(task.__dict__)

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


def find_task_based_on_priority(priority):
    for task in tasklist:
            if(task.priority == priority):
                print_task_details(task)

def sort_tasks():
    sorted_tasks = sorted(tasklist, key=lambda x: x.priority)  
    print("\nSorted Tasks by Priority:")
    for task in sorted_tasks:
        print_task_details(task)

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
      elif(type_of_function == "filter tasks based on priority"):
          priority_number = int(input("Insert the number of priority "))
          find_task_based_on_priority(priority_number)
      use_task_manager = input("Do you need to use the task manager?")



    
         











