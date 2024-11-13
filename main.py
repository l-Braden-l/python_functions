# Braden Leach
# nov 13 2024
# Practice: Positional & Keyword Arguments in Python


# POSITIONAL ARGUMENTS
# Start by writing the code to create the three functions outlined below
# You'll use only positional arguments in the first three functions
# Test your code and correct any errors

# Greet The User
# Write a function that takes two parameters -- first name and age
# Use an f-string to welcome the user by first name and to display his/her age
def greet_user(first_name, age):
    print(f'Hello, {first_name}! you are {age} years old!')

    #call the function/invoke the function 
greet_user('Braden',18)



# Area of a Rectangle
# Write a function to calculate the area (in square feet) of a rectangle
# Your two parameters will be length and width
# The print statement in the function should display the length, width and area (in square feet) of your rectangle
def area_rect(length,width):
    area = length * width
    print(f'The length of the rectagle is {length}, the width is {width} and area (in square feet) is {area} feet!')

#call the function/invoke the function 
area_rect(5,5)



# Sum of Numbers
# Write a function that finds the sum of three numbers
# Your three parameters will be num1, num2, and num3
# The print statement in the function should display the sum of the three numbers
def sum_num(num1,num2,num3):
    sum = num1 + num2 + num3
    print(f'The sum of the three numbers is {sum}.')
    
#call the function/invoke the function 
sum_num(77,8,14)



# KEYWORD ARGUMENTS
# Create the three functions outlined below
# In these last three functions, you'll use only keyword arguments 
# Test your code and correct any errors

# Greet By Title
# Write a function that greets the user by title, first name and last name
# Examples of titles include: Mr., Ms., Mrs. and Dr.
# When calling your function, change the order of your keyword arguments so that they don't match the order of your function parameters
def title(title,first_name,last_name):
    print(f'Hello, your full title is {title}{first_name} {last_name}!')

#call the function/invoke the function 
title(title= 'Mr.', last_name='Fisher',first_name= 'Chad' )



# Describe Your Pet
# Write a function that says what type of pet you have and what your pet's name is
# Your function parameters will be pet_type and pet_name

def describe_pet(pet_type,pet_name):
    print(f'My {pet_type} is {pet_name}!')

    #call the function
    describe_pet(pet_type='cat', pet_name='Jasper')


# Updated Function
# Choose any ONE of the first three functions from this project and rewrite it below using keyword arguments
def area_rect(length,width):
    area = length * width
    print(f'The length of the rectagle is {length}, the width is {width} and area (in square feet) is {area} feet!')

#call the function/invoke the function 
area_rect(width=15,length=8)
