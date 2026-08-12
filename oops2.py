#Create a Student class with name ,age,marks and methods displaydetails and ispass if marks>= 40
class Student:
    def __init__(self,name,age,marks):
        self.name =name 
        self.age =age
        self.marks = marks

    def display_details(self):
        print(f"{self.name} he/she is {self.age} old has secured {self.marks} marks")

    def ispass(self):
        if self.marks>=40:
            print("Passed")

        else:
            print("Failed")

student1 = Student("Pratham",18,90)

student1.display_details()
student1.ispass()
student1.marks = 35
student1.ispass()



# creating a ola/uber using oops as a real world problem project

class Passenger:
    def __init__(self,name,location):
        self.name =name
        self.location = location

class Driver:
    def __init__(self,name,vehicle,location,available):
        self.name = name 
        self.vehicle = vehicle
        self.location = location 
        self.available = True


    def accept_ride(self):
        if self.available:
            print("accepted")
            self.available = False

        else:
            print("Not accepted")

    def complete_ride(self):
        self.available = True

class Ride:
    def __init__(self,passenger,driver,distance):
        self.passenger = passenger
        self.driver = driver
        self.distance = distance
        self.fare = 0 
        self.status= "Requested"

    def calculate_fare(self):
        basefare =25
        per_km = 15
        self.fare = basefare + (self.distance*per_km)
        return self.fare




p1 = Passenger("Pratham","Kundapura")
d1 = Driver("suresh","tata","Tallur",True)

r1 = Ride(p1,d1,100)

print(r1.driver.name)

print(r1.status)
print(r1.calculate_fare())