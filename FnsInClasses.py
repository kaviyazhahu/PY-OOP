#Variables
emp1 = ["TA","name1",29,"S",1500]
emp2 = ["TA","name2",25,"J",1000]

# def code(emp):
#     print(f"{emp[1]} is a TA.")
# code(emp2)

#class
class Office:
    #Class Attribute
    alias = "Class Attribute"

    def __init__(self,name,age,level,salary) :
        #Instance Attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    
    #Instance Method's
    def code(self):
        print(f"{self.name} is a TA.")
    
    def language(self, lannguage):
        print(f"{self.name} writing code in ..... {lannguage}")
    
    #Special Methos
    def __str__(self) -> str:
        information=f"name={self.name},age={self.age},level={self.level}"
        return information
    
    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name and self.age ==  __o.age
    
    ## Static Method
    @staticmethod
    def salary(age):
        if age < 25:
            return 25000
        if age < 30:
            return 30000


#Instance

ob1 = Office("name1",29,"S",1500)
ob2 = Office("name1",29,"S",1500)

print(ob1.name,ob1.age,ob1.level,ob1.salary)
print(Office.alias)

# ob1.code()
# ob1.language("Python")
print(ob1)
print(ob1 == ob2)

#Calling Static Methods by using Class name not by the instance
print(Office.salary(29))

#Recap
# Instance Method
# arguments and can return values
# Special "dunder" methods 
# #Statice Methods