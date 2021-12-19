# Inherits, extends, override

class Employee: #Base Class
    def __init__(self, name , age,  salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary
    def work(self):
        print(f"{self.name} is working...")


class SoftwareDeveloper(Employee):
    def __init__(self, name, age, salary, level) -> None:
        super().__init__(name, age, salary)
        self.level = level    
    def Coding(self):
        print(f"{self.name} is coding ...")
    
    def work(self):
        print(f"{self.name} is working ... from SD")

class Designer(Employee):

    def drawing(self):
        print(f"{self.name} is Drawing ...")
    def work(self):
        print(f"{self.name} is working... from DES")

    

se=SoftwareDeveloper("Kavi","29",29000,"J")
print(se.name,se.age,se.salary)
se.work()
#print(se.level)
se.Coding()

d=Designer("Jhon","29",30000)
print(d.name,d.age,d.salary)
d.work()
d.drawing()



# Polymorphism

print("\n +++ Polymorphism +++ \n")

emp=[SoftwareDeveloper("Kavi","29",29000,"J"),
     SoftwareDeveloper("Kavi","29",29000,"J"),
     Designer("Jhon","29",30000)]    

def motivate_emp(emp):
    for list in emp:
        list.work()

motivate_emp(emp)


# Recap
# Inhertance : ChildClass(BaseClass)
#Inherit,Extend,Override
#Super().__init()__ 
#Polymorphism

#https://www.tutorialsteacher.com/python/public-private-protected-modifiers