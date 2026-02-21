import sys #biblioteka s info o systeme i modulax(biblioteka)
import inspect #introspekciya funkcii
import math #matematika

def add(a:int, b:int) -> int:
    return a+b

print(inspect.getdoc(add)) #dayet dokumentaciyu k funkcii
print(inspect.signature(add)) #dayet arqumenti i vozvrawaemie znacheniya
print(inspect.getsource(add)) #ves kod funkciyi

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        def info(self):
            return f"{self.name}:{self.grade}"

print(inspect.getdoc(Student)) #dayet dokumentaciyu k funkcii
print(inspect.signature(Student)) #dayet arqumenti i vozvrawaemie znacheniya
print(inspect.getsource(Student)) #ves kod funkciyi

members = inspect.getmembers(math)
for name, obj in members:
    if inspect.isfunction(obj):
        print(name)

print(inspect.getdoc(math.sqrt)) #dayet dokumentaciyu k funkcii
print(inspect.signature(math.sqrt)) #dayet arqumenti i vozvrawaemie znacheniya
print(inspect.getsource(math.sqrt)) #ves kod funkciyi
















# print(sys.version) #versiya sistemi
# print(sys.platform) #platforma sistemi

# #vse zaqrujenniye moduli
# print("All modules")
# for module_name in list(sys.modules.keys()):
#     print(module_name)

# print("All paths")
# for path in sys.path:
#   print(path)
