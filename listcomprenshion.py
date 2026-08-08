#Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.
kannada_foods =["mysorepark","laddu","mohanladu"]
upper_food =[food.upper() for food in kannada_foods]
print(upper_food)

#Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop.
it_ems = {"bmw":23,"audi":45,"kia":45,"ford":21}
total =0
for i in it_ems.values():
    total+=i
print(total)

#Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.
numbers=[num for num in range(1,11) ]
print(numbers)
sq_num = [i**2 for i in numbers]
print(sq_num)

#Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. Loop through the list and print each student's information.
student_details = [{"name":"pratham","age":18,"marks":90},{"name":"vivek","age":14,"marks":92},{"name":"ravi","age":48,"marks":98}]
for  student in student_details:
    print(student['name'])




city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
l_city = {s:r for s,r in city_population.items() if r>23}
print(l_city)

rows = 3

# Fix: Place the closing bracket for list(map(...)) before the for loop
matrix = [list(map(int, input().split())) for i in range(rows)]

print(matrix)


