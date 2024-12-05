def task():
  tasks = []
  print("Welcome to to-do-app")
  while True:
    operations = int(input("Enter\n1-Add\n2-Update\n3-Delete\n4-view\n5-exit\n"))
    if operations == 1:
      task_name = input(f"Enter task = ")
      task_name = task_name.lower()
      tasks.append(task_name)
      print(f"your tasks are\n {tasks}")
    elif operations == 2:
      if len(tasks) == 0:
        print("No tasks found")
        continue
      elif len(tasks) > 0:
        update_task = input("Enter task to be updated = ")
        update_task = update_task.lower()
      if update_task not in tasks:
        print("Task not found")
        update_task = input("Enter task to be updated = ")
        update_task = update_task.lower()
      for i in range(len(tasks)):
          if tasks[i] == update_task:
            tasks[i] = input("Enter new task = ")
            tasks[i] = tasks[i].lower()

      print(f"{tasks[i]} has been successfully updated")

    elif operations == 3:
      if len(tasks) == 0:
        print("No tasks found to delete")
        continue
      delete_task = input("Enter task to be deleted = ")
      delete_task = delete_task.lower()
      if delete_task not in tasks:
        print("Task not found")
        delete_task = input("Enter task to be deleted = ")
        delete_task = delete_task.lower()
      tasks.remove(delete_task)
      print(f"{delete_task} has been successfully deleted")

    elif operations == 4:
      if len(tasks) == 0:
        print("No tasks found")
      else:
        print(f"your tasks are\n {tasks}")
    elif operations == 5:
      break
    elif operations > 5 or operations <1:
      print("Invalid input")

task()

