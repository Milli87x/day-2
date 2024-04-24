#day 2: 30 days of python
# level 1
#declaring multiple variables in a single line
first_name,last_name,full_name,country,city,Age,year,is_married,is_true,is_light_on = 'Milliyon','Gebrehiwot','Milliyon Gebrehiwot','Ethiopia','Addis Ababa',23,2016,False,True,'yes'
print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(Age)
print(year)
print(is_married)
print(is_true)
print(is_light_on)

''' level 2 --Check the data type of all your variables using type() built-in function
Using the len() built-in function,find the length of your first name
Compare the length of your first name and your last name
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords'''

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(Age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))


A = len(first_name)
B = len(last_name)
print('first name length is',A)
print('last name length is',B)
print('the difference in length is',((A)-(B)))

num_one = 5
num_two = 4

total = num_one+num_two
diff = num_two-num_one
product = num_one*num_two
division = num_one/num_two
variable_remainder = num_two%num_one
exp = num_one**num_two
floor_division = num_one//num_two

#calculating radius and circumference of a circle
# measurement in meters

pi = 3.14159
radius = 30 
area_of_circle = pi*radius**2
circum_of_cirlce = 2*pi*radius

print(area_of_circle)
print(circum_of_cirlce)

#we can also import the librery 'math' and use pi from the libraray
#taking user input for radius

import math
new_PI = math.pi
Radius_ = float(input('enter the radius'))

Area_of_Circle = new_PI*Radius_**2
circumference = 2*new_PI*Radius_
print('the area of the circle is',Area_of_Circle)
print('the circumference is',circumference)



#takin user input for first name,last name, country and age(float func for numbers)


firstname=input()
lastname=input()
yourcountry=input()
age=float(input())
