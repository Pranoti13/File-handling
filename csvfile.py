import csv                      #csv is module to handle csv file
with open("emp.csv","w",newline="")as f:
    w=csv.writer(f)             #returns csv writer object
    w.writerow(["ENO","ENAME","ESAL","EADDR"])
    n=int(input("enter num of emp:"))
    for i in range(n):
        eno=input("enter emp no:")
        ename=input("enter emp name:")
        esal=input("enter emp sal:")
        eaddr=input("enter emp add:")
        w.writerow([eno,ename,esal,eaddr])
print("total emp data written to csv file succesfully")