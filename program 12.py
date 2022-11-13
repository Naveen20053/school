import csv
def user():
    with open("user.csv", "w") as o:
        file = csv.writer(o)
        file.writerow(["User Id", "password"])
        n = int(input("how many ids do you want to enter? "))
        for i in range(n):
            
            user_id = input("enter username: ")
            password = input("enter password: ")
            record = [user_id, password]
            file.writerow(record)
           
    with open("user.csv", "r") as s:
        readed = csv.reader(s)  
        wt = input("enter the user id to be searched: ")
        exist=False
        for id in readed:
            next(readed)
            if id[0] ==wt:
                print(f"Your password is: {id[1]}")
                exist=True
    if exist==False:
        print("the username doesnt exist")

            
user()
