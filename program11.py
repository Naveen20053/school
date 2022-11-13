import csv
def stu():
    f1 = open("Student.csv", "w+")
    stu_det = csv.writer(f1)
    Record = ("Roll.No" , "Name" , "Marks")
    stu_det.writerow(Record)
    n = int(input("how many records do u want to enter? "))
    for student in range(n):
        print("Student Record", (student+1))
        rollno = int(input("what is your roll no? "))
        name = input("what is your name? ")
        marks = float(input("what is your marks?: "))
        sturec = [rollno, name, marks]
        stu_det.writerow(sturec)
    f1.close()
  
    with open("student.csv", newline = "\r\n")as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)
    
    
stu()
