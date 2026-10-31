# 1.
# def is_even(n):
#     if n%2 == 0:
#         print("The number is Even!")
#     else:
#         print("The number is Odd!")
# is_even(41)

# 2.
# def large_no(a,b):
#     if a > b:
#         print(f"The {a} is larger number than {b}")
#     else:
#         print(f"The {b} is larger number than {a}")
# large_no(24,32)

# 3. 
# def print_no(n):
#     n = int(input("Enter the no.: "))
#     for i in range(n, n+1):
#         n += i
#         print("The no. is ", i)
# print_no(23)

# 4. 
# n = 0
# def sum_n():
#     n = int(input("Enter the number whose want to sum: "))
#     return n * (n+1) // 2

# print(sum_n())

# 5. 
# def table():
#     n = int(input("Enter the no. of table you want: "))
#     for i in range(1, 11):
#         print(f"{n} x {i} = {n*i}")
# table()

# 6. 
# def count_even(n):
#     return sum(1 for num in n if num % 2 == 0)
# print(count_even([3,45,6,4,3,2,6,2]))

# 7. 
# def largest_no(n):
#     largest = n[0]
#     for num in n[1:]:
#         if num > largest:
#             largest = num
#     return largest

# print(largest_no([10,39,49,58,66,3,6]))

# 8. 
# def fizzbuzz():
#     for i in range(0,101):
#         if i % 3 == 0:
#             print("fizz",i)
#         elif i % 5 == 0:
#             print("Buzz",i)
#         else:
#             print("fizzBuzz",i)
# fizzbuzz()

# 9. 
# def palindrom(string):
#     t = str(string)
#     left = 0
#     right = len(t) - 1

#     while left < right:
#         if t[left] != t[right]:
#             return False
#         left += 1
#         right -= 1

#     return True
# print(palindrom("madam"))

# 10. 
# def vowels():
#     s = input("Enter the word: ")
#     vowel = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowel:
#             count +=1
#     return count

# print(vowels())

# 11. 
# def second_large(n):
#     largest_no = n[1]
#     for i in n[:-1]:
#         if i > largest_no:
#             largest_no = i
#     return largest_no
# num = [10,29,48,58,69]
# print(second_large(num))

# 12.
# import random 
# def guessing_game():
#     n = random.randint(1,10)
#     while True:
#         guess  = int(input("Enter the number between 1-10: "))
        
#         if guess == n:
#             print("You guess the right number...")
#             break
#         elif guess > n:
#             print("The value is high, guess the low value!")
#         else:
#             print("The value is low, guess the high value!")
# guessing_game()

# 13. 
# def grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 80:
#         return "B"
#     elif marks >= 70:
#         return "C"
#     elif marks >= 60:
#         return "D"
#     else:
#         return "F"
# print(grade(10))


