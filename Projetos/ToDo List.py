# 1. Settings
todo_list = []
time = []

# 2. Loop
while True:

# 3. Checks list
  if len(todo_list) == 0:
    print("Your ToDo list is empty")

# 4. Print
  else:
    index = 1
    print("\nToDo list:")
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1

# 5. Options
  print("\nOptions:\n1) Add Task\n2) Remove Task\n3) Quit")
  choice = input("\nSelect your choice: ")
  if choice == "1":
    new_task = input("Enter a task: ")
    todo_list.append(new_task)
    print(f"The task '{new_task}' has been added to the list")
  elif choice == "2":
    if todo_list == []:
      print("Your ToDo list is already empty")
    else:
      todo_list.pop()
  elif choice == "3":
    print("\nQuitting")
    break
  else:
    print("This is not a valid option")