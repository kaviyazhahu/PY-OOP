#Variables
emp1 = ["TA","name1",29,"S",1500]
emp2 = ["TA","name2",25,"J",1000]

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


#Instance 

ob1 = Office("name1",29,"S",1500)

print(ob1.name,ob1.age,ob1.level,ob1.salary)
print(Office.alias)

#Recap
# Create a Class
# Create a instance (Object)
# class vs instance 
# instance attributes : defined in __init()__ (self )   
# Class Attribute