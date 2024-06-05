 #Data types
#strings
"Hello"[4]

#Integer
123

#float
3.14159

#Boolean
True
False 

num_char = len(input("What is your name? "))
print("Your name has" + num_char + "characters.")

#Type checking
print(type(num_char)) 

#Type conversion
new_num_char =str(num_char)
print("Your name has" + new_num_char + "characters.")

a = float(123)
print(type(a))

print(70 + float("100.5"))

two_digit_number = input("write two numbers ")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
two_digit_number = first_digit + second_digit
print(two_digit_number)

''' Mathematical operations
PEMDASLR
Parenthesis ()
Exponient **
Multiplication *
Division /
Addition +
Subtraction - '''

print(3 * 3 + 3 / 3 - 7) 

weight = int(input("What is the weight of the person? "))
height = float(input("What is the height of the person? "))
body_mass_index = weight / (height ** 2)
body_mass_index = int(body_mass_index) 
print(body_mass_index) 


#Number Multiplication 
#/ gives a format
#// gives a whole number 
print(round(8 / 3,2))
print(8 // 3) 
score = 2
score += 2
print(score) 

#F strings
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}. your height is {height}, you are winning is {isWinning}") 
 
age = int(input("What is your age? "))
years = 90 - int(age)
week = years * 52
print(f"you have {week} weeks left.")




















