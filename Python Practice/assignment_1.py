# 1.

num=float(input("Enter the no.: "))

if num > 0:
    print("The no. is Positive!")
elif num < 0:
    print("The no. is Negative!")
else:
    print("The no. is zero")


# 2. 

num=int(input("Enter the no.: "))

if num % 2 == 0:
    print(" the no. is Even!")
else:
    print("The no. is Odd!")

# 3.

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

if n1 > n2:
    print("The first number is greater.")
elif n2 > n1:
    print("The second number is greater.")
else:
    print("Both numbers are equal.")


# 4.

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

if n1>n2 and n1>n3:
    print("The first number is the greatest.")
elif n2>n1 and n2>n3:
    print("The second number is the greatest.")
else:
    print("The third number is the greatest.")


# 5. 
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# 6.
year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a leap year.",year)
else:
    print("This is not a leap year.",year)
    
# 7.
char = input("Enter a character: ").lower()

if char in ["a", "e", "i", "o", "u"]:
    print("The character is a vowel.")
else:
    print("The character is a consonant.")

# 8.
num = int(input("Enter a number: "))

if num % 5==0 and num % 11==0:
    print("The number is divisible by both 5 and 11.")
else:
    print("The number is not divisible by both 5 and 11.")

# 9.
num = int(input("Enter a number: "))

if num % 3 ==0 and num % 7 ==0:
    print("The number is divisible by both 3 and 7.")
else:
    print("The number is not divisible by both 3 and 7.")

# 10.
sub = float(input("Enter marks for subject: "))

if sub >= 90 and sub <= 100:
    print("Grade: A")
elif sub >= 80 and sub < 89:
    print("Grade: B")
elif sub >= 70 and sub < 79:
    print("Grade: C")
elif sub >= 60 and sub < 69:
    print("Grade: D")
else:
    print("Grade: F")


# 11.
char = input("Enter a character: ")

if char.islower():
    print("The character is in lowercase.")
else:
    print("The character is in uppercase.")

# 12.
alphabet = input("Enter an alphabet: ").lower()

if alphabet in "a":
    print("this alphabet is vowel a.")
elif alphabet in "e":
    print("this alphabet is vowel e.")
elif alphabet in "i":
    print("this alphabet is vowel i.")
elif alphabet in "o":
    print("this alphabet is vowel o.")
elif alphabet in "u":
    print("this alphabet is vowel u.")
else:
    print("this alphabet is consonant.")


# 13.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a+b>c and a+c>b and b+c>a:
    print("The numbers can form a triangle.")
else:
    print("The numbers cannot form a triangle.")


# 14.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))


if a==b==c:
    print("The triangle is equilateral")
elif a==b or b==c or a==c:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")


# 15.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

if a > b and a > c and a > d:
    print("The first number is the greatest.")
elif b > a and b > c and b > d:
    print("The second number is the greatest.")
elif c > a and c > b and c > d:
    print("The third number is the greatest.")
else:
    print("The fourth number is the greatest.")


# 16.
a = int(input("Enter the three-digit number: "))

if a <= 100 or a >= 999:
    print("The number is not a three-digit number.")
else:
    print("The number is a three-digit number.")
    

# 17.
units = float(input("Enter the number of units consumed: "))
 
if units <= 100:
    bill = units * 5
elif units <=200:
    bill = (100 * 5) + ((units - 100) * 7)
elif units <= 300:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
else:
    bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 15)

print("The Bill is: ",bill)

# 18.

income = float(input("Enter your income: "))

if income <=250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (income - 500000) * 0.2 + (250000 * 0.05)
else:
    tax = (income - 1000000) * 0.3 + (500000 * 0.2) + (250000 * 0.05)

print("The income tax is: ",tax)

#19. 
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))

if sub1 >=35 and sub2 >=35 and sub3 >=35:
    print("The student has passed.")
else:
    print("The student has failed.")
    
#20.

num = int(input("Enter a number: "))

range = 1 <= num <= 100

if range:
    print("The number is in the range of 1 to 100.")
else:
    print("The number is not in the range of 1 to 100.")

# 21. 
a = int(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
b = int(input("Enter the second number: "))

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero!"
else:
    result = "Error: Invalid operator!"

print("The result is: ", result)

# 22. 
year = int(input("Enter the year: "))

if year % 100 == 0 and year % 400 == 0:
    print("The year is a century leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")
    

# 23. 
month = int(input("Enter the month (1-12): "))

if month in [2,3,4,5]:
    season = "Summer"
elif month in [6,7,8,9]:
    season = "Rainy"
elif month in [10,11,12,1]:
    season = "Winter"   
else:
    season = None
    print("The month is not valid.")

print("The season is: ", season)


# 24. 
month = int(input("Enter the month"))
year = int(input("Enter the year"))

if month in [1,3,5,7,8,10,12]:
    print("The days are 31")
elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("The days are 29")
    else:
        print("The days are 28")
elif month in [4,6,9,11]:
    print("The days are 30")

else:
    print("The invalid month")

# 25. 
password = input("Enter your password: ")

if len(password) < 8:
    print("Password  contain at least 8 characters.")

elif not any(char.isdigit() for char in password):
    print("Password  contain at least one digit.")

elif not any(char.isupper() for char in password):
    print("Password  contain at least one uppercase letter.")

elif not any(char.islower() for char in password):
    print("Password  contain at least one lowercase letter.")

elif not any(not char.isalnum() for char in password):
    print("Password  contain at least one special character.")

else:
    print("Password meets all minimum conditions!")


# 26. 

age = int(input("Enter your age: "))

ticket_price = 50

if age <=10:
    ticket_price =age * 0.5
elif age >= 11 and age <=59:
    ticket_price = 50
elif age >= 60:
    ticket_price = age * 0.5
else:
    ticket_price = 50

print("The ticket price is: ", ticket_price)

# 27. 

amount = int(input("Enter purchase amount: "))

if amount >= 10000:
    discount = amount * 0.20

elif amount >= 5000:
    discount = amount * 0.10

elif amount >= 2000:
    discount = amount * 0.05

else:
    discount = 0

final_amount = amount - discount

print("Purchase Amount: ", amount)
print("Discount: ", discount)
print("Final Amount: ", final_amount)


# 28.
age  = int(input("Enter the age: "))
eyesight = input("Is your eyesight normal? (yes/no): ").lower()

if age >= 18 and eyesight == 'yes':
    print("You are eligiable for drivinng license!")
else:
    print("Sorry,You are not eligiable for driving license!")

# 29.
username = input("Enter your username: ")
password = input("Enter your password: ")

username_ = "admin"
password_ = "admin123"

if username == username_ and password == password_:
    print("Login successful!")
else:
    print("Invalid username or password.")

# 30.

a = int(input("Enter the a: "))
operation = input("Enter the operation: ").lower()
b = int(input("Enter the b: "))

if operation == "addition":
    print(a + b)
elif operation == "subtraction":
    print(a - b)
elif operation == "multiplication":
    print(a * b)
elif operation == "division":
    if b != 0:
        print(a / b)
    else:
        print("Sorry, b is zero!")
elif operation == "exit":
    print("Exit the program...")
    
else:
    print("Invalid operation type!") 

