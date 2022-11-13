import csv
def det():
    f= open("details.csv" ,"w") 
    file = csv.writer(f)
    file.writerow(["Dept Id", "Name", "City"])
    n = int(input("how many details do you want to enter? "))
    for i in range(n):
        dept_id = input("Enter a dept_Id: ")
        name = input("Enter a name: ")
        city = input("Enter a city: ")
        record = [dept_id , name, city]
        file.writerow(record)
    f.close()
def search():
    k= open("details.csv")
    j = csv.reader(k)
    wt = input("enter the dept id of the record you want: ")
    exist = False
    for id in j:
        next(j)
        if wt==id[0]:
            print (f"dept id: {id[0]}, name is: {id[1]}, and city is: {id[2]}")
            exist=True
    if exist==False:
        print("doesnt exist")                   
    
while True:
    ch_1 = print("1. Create Csv File")
    ch_2 = print("2. Search")
    ch_3 = print("3. Stop")
    ch = int(input("choose  a choice: "))
    if ch == 1:
        print("---CREATING---")
        det()
    elif ch == 2:
        print("---SEARCHING---")
        search()
    elif ch  == 3:
        print("your program ended ")
        break
    else:
        print("Enter a Valid Input")
