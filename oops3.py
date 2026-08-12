#Getters, Setters, Method Overloading & Overriding, super(), Abstract Classes
class Student:
    def __init__(self,marks):
        self.__marks =marks

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if self.__marks>=100:
            self.__marks= marks


a = Student(100)
a.set_marks(100)
print(a.get_marks())



# calculator using default aguments or *args

class Calculator:
    def add(self, *numbers):
        c =0
        for i in numbers:
            c+=1
        return c
    def show(self,*numbers):
        return numbers
b = Calculator()
print(b.show(23,34,45,700,900,8))
    
    