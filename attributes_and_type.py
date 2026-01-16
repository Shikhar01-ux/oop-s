#Class atribute belongs to class. It is common.It can be acess from class name 
#Instance belong to object. It is unique

class student():
    college_name = "Shri Ramswaroop Memorial University"

    def __init__ (self,name,roll_no):
        self.name = name 
        self.roll_no = roll_no

stu1 = student("Shikhar yadav", 202510101240087)
stu2 = student("Sovind yadav", 202510101240070)
print(f"Name of student first is {stu1.name} and Roll number is {stu1.roll_no} and college is {student.college_name}")