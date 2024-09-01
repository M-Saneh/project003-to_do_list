def task():
    tasks = []  #this is an empty list
    print("======WELCOME-TO-TASK-MANEGER-APP======")

    total_task = int(input("Enter the number of tasks you want to add :")) #5
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = ")  # will be seen as -->enter task 1 = 
        tasks.append(task_name)
    print(f"today's tasks are\n{tasks}")    

    while True:
        operation = int (input("Enter\n1-To Add\n2-To update\n3-To Delete\n4-To View\n5-To Exit or stop"))
        if operation == 1:
            add = input("Enter task you want to Add = ")
            tasks.append(add)
            print(f"The task {add} has been successfully added ...")
        elif operation == 2:
            updated_val = input("Enter the task name you want to update =")  
            if updated_val in tasks:
                up = input("Enter the new task =")
                ind = tasks.index(updated_val) # using indexing yo find the task that the user had intered
                tasks[ind] = up #update th new task
                print(f"Updated task {up}")
        elif operation == 3:
            del_val = input("Which task do you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted")
        elif operation == 4:
            print(f"total tasks are {tasks}")  
        elif operation == 5:
            print("closing the program...")          
            break
        else: 
            print("invalid input:") #if user inputs neither 1,2,3, etc ,"an invalid input" promt will be shown

task()




