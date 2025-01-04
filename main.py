"""This is a program to write TO DO List, user can add, delete, make completed, and view tasks"""
import random
"""functios"""
def main():
    message="""1-add task
    2-mark task as completed
    3-delet task
    4-view tasks
    5-quit"""
    
    while True:
        print(message)
        choice=int(input("Enter your choice: "))
        # tasks(tasks_list)
        if choice==1:
            #add tasks
            add_task()
            
        elif choice==2:
            mark_task_completed(tasks_list)
            
        elif choice==3:
            delete_task()
            
        elif choice==4:
            view_tasks(tasks_list)
            
        elif choice==5:
            break #quit the program
        
        else:
            print("invalid choice, please enter number between 1 and 5")

        print("_"*30)    
def tasks(tasks):
    """tasks function takes 2d list and print its items to show the to do list"""
    print("To Do List")
    k=0 #for encrementing
    for task in tasks: #for loop for tasks 
        k+=1

        print(f"{k}-{task[0]}")        
def add_task():
    """function that add task to tasks list """
    #get task
    
    task=input("Enter task: ")
    
    #task status
    
    task_info=[task, False]
    
    #add task to tasks
    
    tasks_list.append(task_info)
     
    print("Task add successfully!")
def cross(text):
    """this function to cross strings"""
    
    return ''.join(char + '\u0336' for char in text)       
def mark_task_completed(tasks_list):
    f=[] #incompleted list
    for incom in tasks_list:
        
        if incom[1]==False:
            f.append(incom)
                 
    tasks(f)

    #user choose completed task
    if f !=[]:
        try:
            task_num=int(input("Enter the completed task number: "))
            
            if task_num<1:
                print("Enter +ve number!")
                return
            
            #completed tasks to true
            f[task_num-1][1]=True
            #cross deleted tasks
            m=["Good job!","Well done!!", "Wow", "Yaaaay", "Task is done", "<3"]
            r=random.choice(m)  #choice random message from list m to display
            print(r)
        except IndexError as e:
            print(e, "Enter number of tasks range")    
        except ValueError as e:
            print(e,"Enter number!")
        except Exception as e:
            print(e)
            
            
    
    else:
        
        print("No more tasks for today!!\n","Enjoy<3")
        return        
def delete_task():
    tasks(tasks_list)
    """function to delete task from tasks list"""
    #number of task to delete
    task_num=int(input("Enter which task number you want to delete: "))
    #delete task
    tasks_list[task_num-1][0]=cross(tasks_list[task_num-1][0])
    
    tasks_list[task_num-1][1]=""
    
    print(f"task {task_num} is deleted")  
def view_tasks(tasks_list):
    """function to see all tasks"""
    if len(tasks_list)>0:
        
        print("To Do List")
        k=0 #for encrementing
        for task in tasks_list: #for loop for tasks 
            k+=1
            if task[1]==False:
                print(f"{k}.{task[0]} ❌")
                
            elif task[1]==True:
                print(f"{k}.{task[0]} ✔️")
                
            elif task[1]=="":
                print(f"{k}.{task[0]}")
        
        
    else:
        print("You have no tasks to view")
        return

"""CODE"""
tasks_list=[] #list of tasks

if __name__=="__main__":
    main()



