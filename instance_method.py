'''
There are three type of methods in oop's
1- Instance
2- Class
3- Static

'''
class laptop():
    storage_type = "SSD"

    def __init__(self,RAM,storage):
        self.RAM = RAM 
        self.storage = storage

    def get_info(self):  #Instance method 
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type} Storage")


l1 = laptop("16gb", "512GB")
l1 = laptop("8gb", "256GB")

l1.get_info()