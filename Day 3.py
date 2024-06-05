#Conditional(if/else statements)
num = int(input("Enter a number "))
number = num
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number") 


#EXERCISE
height = float(input("What is your height? "))  
weight = int(input("What is yor weight? "))
body_mass_index = round(weight / (height * 2),2)
if body_mass_index < 18.5:
    print(f"Your body_mass_index is {body_mass_index}, You are underweight")
elif body_mass_index <= 25:
    print(f"Your body_mass_index is {body_mass_index}, You have a normal weight")
elif body_mass_index <= 30:
    print(f"Your body_mass_index is {body_mass_index}, You are slightly overweight")
elif body_mass_index <= 35:
    print(f"Your body_mass_index is {body_mass_index}, You are obese") 
else:
    print(f"Your body_mass_index is {body_mass_index}, You are clinically obese") 


#EXERCISE
year = int(input("Pick a year "))
leap_year = year
if leap_year % 4 == 0:
    if leap_year % 100 == 0:
        if leap_year % 400 == 0:
            print("Leap year")
        else: 
            print("Not leap year")
    else: 
        print("Leap year")
else:
    print("It is not a leap year") 

#OR
year = int(input("Pick a year "))
leap_year = year
if leap_year % 4 == 0:
    print("Leap year")
if leap_year % 100 == 0:
    print("Leap year")
if leap_year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year") 
 

#EXERCISE
#PIZZA ORDER PROGRAM
print("Thank you for choosing pizza deliveries!")
size = input("What size of pizza do you want? S,M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
else:
    bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}") 

#LOGICAL OPERATORS
print("Welcome to the rollercoaster!")
height = int(input("What is the height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay, Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want photo taken? Y or N.  ")
    if wants_photo == "Y":
        bill = bill + 3    #or bill += 3

        print(f"Your final bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride!") 

#EXERCISE
#LOVE CALCULATOR
print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
combined_name = name1 + name2 
lover_name = combined_name.lower()
t = lover_name.count("t")
r = lover_name.count("r")
u = lover_name.count("u")
e = lover_name.count("e")
first_digit = t + r + u + e

l = lover_name.count("l")
o = lover_name.count("o")
v = lover_name.count("v")
e = lover_name.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
    

        
