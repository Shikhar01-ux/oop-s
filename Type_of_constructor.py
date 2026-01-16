class student():
    def __init__(self, name, year): #Parameterized constructor Bacause it has multiple constructor 
        self.name = name            #apart from the self constructor 
        self.year = year

    def get_name(self):
        return self.name

stu1 = student("Shikhar yadav",1)
stu2 = student("Sovind Yadav",1)

print(f"Name of first student is {stu1.get_name()}")
