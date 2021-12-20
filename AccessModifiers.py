class student:
    schoolName = "SMS" #Class Attribute
    _mobile=9600570809

    def __init__(self, name, age) -> None:
        #Public
        self.name = name #instance Attribute
        self.age = age
        #Protected
        self._email = "kaviyazhahu@gmail.com"
        #Private
        self.__aadhar="XXXX XXXX XXXX XXXX"
    def __display_aadhar(self):
        print("Printing AADHAR No from Provate MEthod",self.__aadhar)

## Access Public/Protected    
std =student("kavi","28")
print(std.name,std.age,std._email,student._mobile)

### Access Private Members. syntax : _object._class__variable
print(std._student__aadhar)
std._student__display_aadhar()