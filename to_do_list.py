import time as t
TASK=[]
d="done"
nd="not done"
while True:
    print("======TO DO LIST======")
    print("\n\t1.Create Task\n\t2.Track Task\n\t3.Update Task\n\t4.Exit")
    choice=int(input("Enter the choice:\n"))
    if choice==1:
        n=int(input("Enter the number of Tasks to add:\n"))
        for i in range(n):
            task=input("Enter the task: ")
            TASK.append({"task":task,"status":nd})
            print("Task added.")
    elif choice== 2:
        print("Tasks:")
        i=1
        for _ in TASK:
            if _["status"]==nd:
                status = nd
            else:
                status=d
            print(i,".",_["task"],"-",status,sep=" ")
            i+=1
        print()
    elif choice==3:
        tasks=input("Enter the Task name to Update:\n")
        c=1
        for _ in TASK:
            if tasks==_["task"]:
                _["status"]=d
                print("Update Done")
                c=0
        else:
            if c==1:
                print("Task Not Found")

    elif choice==4:
        t.sleep(.3)
        print("YOUR QUITING THE TO DO LIST")
        t.sleep(.5)
        print("THANK YOU..")
        exit()