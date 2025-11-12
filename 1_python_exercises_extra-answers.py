# Python
# --------------------------------Variables---------------------------------
# Declare two variables, x and y, and assign them the values 5 and 10. Print their sum.
x = 5
y = 10
print(x + y)


# Create a variable name and assign your name to it. Print a greeting using the variable.
name = "Ali"
print(name)

# alternative
name = "Ali"
print(f"Hello, {name}!")


# ----------------------------Conditional Statements-------------------------------
# Write a program that checks if a given number is even or odd.
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Create a program that determines if a student's grade is 'A,' 'B,' 'C,' or 'Fail' based on their score.
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Fail")


# Implement a calculator that performs addition, subtraction, multiplication, or division based on user input.
num1 = 10
num2 = 5
operator = "+"

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")


# ----------------------------Loops---------------------------------
# Write a while loop that prints the square of numbers from 1 to 5.
i = 1
while i <= 5:
    print(i * i)
    i += 1

# Implement a countdown timer using a while loop. Start from 10 and print the countdown value until reaching 1. 
# After reaching 1, print "Happy Birthday!"(only once)
i = 10
while i >= 1:
    print(i)
    i -= 1
print("Happy Birthday!")

# Alternative
i = 10
while True:
    print(i)
    i -= 1
    if i == 0:
        break
print("Happy Birthday!")

# Write a program that prints numbers from 1 to 50. For multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz." 
# For numbers that are multiples of both 3 and 5, print "FizzBuzz."
i = 1
while i <= 50:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1

# alternative
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Write a program that gives you a total of numbers from 1 to 100 -  Answer: 5050
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)

# alternative
total = 0
for i in range(1, 101):
    total += i
print(total)


# Factorial Calculation:
# Implement a program to calculate the factorial of the number  5 using a for loop.
# Answer 120
factorial = 1
i = 1
while i <= 5:
    factorial *= i
    i += 1
print(factorial)

# alternative
factorial = 1
for i in range(1, 6):
    factorial *= i
print(factorial)

# Even Numbers:
# Write a program to print all even numbers between 1 and 20 using a while loop and if condition.
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# alternative
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Pattern Printing:
# Create a program to print the following pattern using loops:

#
##
###
####
#####


i = 1
while i <= 5:
    print("#" * i)
    i += 1

# alternative
for i in range(1, 6):
    print("#" * i)

# Create a program to print the following pattern using loops:

#####
####
###
##
#

i = 5
while i >= 1:
    print("#" * i)
    i -= 1

# alternative
for i in range(5, 0, -1):
    print("#" * i)

# Create a program to print the following pattern using loops:

#     *
#    ***
#   *****
#  *******

i = 1
while i <= 4:
    print(" " * (4 - i) + "*" * (2 * i - 1))
    i += 1

# alternative
for i in range(1, 5):
    print(" " * (4 - i) + "*" * (2 * i - 1))

# general version
n = 4
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# ----------------------------Tuples---------------------------------
# Create a tuple with three integers. Find the sum of the elements.
my_tuple = (1, 2, 3)
print(sum(my_tuple))

# alternative
my_tuple = (1, 2, 3)
total = 0
for i in my_tuple:
    total += i
print(total)

# Find the highest number from a list
my_list = [1, 2, 3, 4]
print(max(my_list))

# alternative
my_list = [1, 2, 3, 4]
max_num = my_list[0] # max_num = float("-inf")
for i in my_list:
    if i > max_num:
        max_num = i
print(max_num)

# Find the second-highest number from a list
my_list = [4, -3,-2,1,1,4]
max_num = float("-inf")
second_max_num = float("-inf")
for i in my_list:
    if i > max_num:
        second_max_num = max_num
        max_num = i
    elif i > second_max_num:
        second_max_num = i
print(second_max_num)

# Find the second (distinct) highest number from a list
my_list = [4, -3,-2,1,1,4]
max_num = float("-inf")
second_max_num = float("-inf")
for i in my_list:
    if i > max_num:
        second_max_num = max_num
        max_num = i
    elif i > second_max_num and i != max_num:
        second_max_num = i
print(second_max_num)

# Define a dictionary with keys 'name', 'age', and 'city'. Print the values.
my_dict = {"name": "Ali", "age": 20, "city": "Baku"}
print(my_dict.values())

# alternative
my_dict = {"name": "Ali", "age": 20, "city": "Baku"}
for key, value in my_dict.items():
    print(value)

# Write a program to print all odd numbers backward from 15 to 1 using a for loop.
for i in range(15, 0, -1):
    if i % 2 != 0:
        print(i)

# alternative
for i in range(15, 0, -2):
    print(i)

# ----------------------------Functions---------------------------------

# Even or Odd Function:
# Write a Python function that takes an integer as input and returns "Even" if it's even and "Odd" if it's odd.
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_or_odd(10))

# Factorial Function:
# Implement a function to calculate the factorial of a given number.
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(5))


# Game:
import random
random_number = random.randint(1, 10)
while True:
   my_guess = int(input("enter your guess: "))
   if my_guess == random_number:
       print("You won!")
       break
   else:
       print("Try again")


# Add two new functionalities to this game:
# The game should give you hints when your guess is wrong. 
import random
random_number = random.randint(1, 10)
while True:
   my_guess = int(input("enter your guess: "))
   if my_guess > random_number:
       print("Too high")
   elif my_guess < random_number:
       print("Too low")
   elif my_guess == random_number:
       print("You won!")
       break
#    else:
#        print("Try again")


# You should only have three chances to guess the number
import random
random_number = random.randint(1, 10)
chances = 3
while True:
   my_guess = int(input("enter your guess: "))
   if my_guess == random_number:
       print("You won!")
       break
   elif chances <= 1:
       print("You lost!")
       break
   elif my_guess > random_number:
       print("Too high")
   elif my_guess < random_number:
       print("Too low")
#    else:
#        print("Try again")
   chances -= 1


# --- count_vowels("Hello World")
def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count
print(count_vowels("Hello World"))


# --- sum_of_digits(12345)
def sum_of_digits(n):
    n = str(n)
    total = 0
    for digit in n:
        total += int(digit)
    return total
print(sum_of_digits(12345))

# alternative
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total
print(sum_of_digits(12345))


# --- find_primes_in_range(10, 20)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
print(find_primes_in_range(10, 20))

# alternative
def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes
print(find_primes_in_range(10, 20))


# --- longest_word_length("The quick brown fox jumps over the lazy dog")
def longest_word_length(sentence):
    words = sentence.split()
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest
print(longest_word_length("The quick brown fox jumps over the lazy dog"))


# --- fibonacci(7)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))


# --- remove_duplicates([1, 2, 2, 3, 4, 4, 5])
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

# alternative
def remove_duplicates(lst):
    uniques = []
    for item in lst:
        if item not in uniques:
            uniques.append(item)
    return uniques
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))


# --- find_anagrams("listen", ["enlist", "google", "inlets", "banana"])
def find_anagrams(word, words):
    anagrams = []
    for item in words:
        if sorted(item) == sorted(word):
            anagrams.append(item)
    return anagrams
print(find_anagrams("listen", ["enlist", "google", "inlets", "banana"]))

# alternative
def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)
def find_anagrams(word, words):
    anagrams = []
    for item in words:
        if are_anagrams(item, word):
            anagrams.append(item)
    return anagrams
print(find_anagrams("listen", ["enlist", "google", "inlets", "banana"]))


# --- is_perfect_square(16)
def is_perfect_square(n):
    return n ** 0.5 == int(n ** 0.5)
print(is_perfect_square(16))

# alternative
def is_perfect_square(n):
    for i in range(n):
        if i * i == n:
            return True
    return False
print(is_perfect_square(16))


# --- longest_unique_substring("abcdpabcbb")
def has_unique_letters(string):
    return len(set(string)) == len(string)

def longest_unique_substring(string):
    longest_substring = ""
    for start in range(len(string)+1):
        for end in range(start, len(string)+1):    
            substring = string[start:end]
            if has_unique_letters(substring):
                if len(substring) > len(longest_substring):
                    longest_substring = substring

    return longest_substring

print(longest_unique_substring("abcdpabcbb"))


# rotate_list([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
def rotate_list(lst, n):
    n = n%len(lst)
    return lst[-n:] + lst[:-n]
print(rotate_list([1, 2, 3, 4, 5], 8))


# is_sorted([1, 2, 3, 4, 5])
def is_sorted(arr):
    return sorted(arr) == arr
print(is_sorted([1, 3, 2, 3, 4, 5]))

# alternative
def is_sorted(arr):
    for i in range(len(arr)):
        if i < len(arr) - 1:
            if arr[i] > arr[i+1]:
                return False
    return True
print(is_sorted([1, 3, 2, 3, 4, 5]))

# alternative
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
print(is_sorted([1, 3, 2, 3, 4, 5]))


# count_frequency([1, 2, 2, 3, 3, 3, 4])
def count_frequency(lst):
    return {item: lst.count(item) for item in lst}
print(count_frequency([1, 2, 2, 3, 3, 3, 4]))

# alternative
def count_frequency(lst):
    freq_dict = {}
    for thing in lst:
        if thing not in freq_dict:
            freq_dict[thing] = 1
        elif thing in freq_dict:
            freq_dict[thing] += 1
    return freq_dict
print(count_frequency([1, 2, 2, 3, 3, 3, 4]))


# bubble_sort([64, 34, 25, 12, 22, 11, 90])  
# link: https://en.wikipedia.org/wiki/Bubble_sort
def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n):
            if i>=1:
                if arr[i-1] > arr[i]:
                    arr[i-1], arr[i] = arr[i], arr[i-1]
                    swapped = True
    return arr
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))


# Input: [1, -2, 0, 3]
# Output: 4
# Explanation: We can delete only one element and obtain the maximum sum of 4
def max_sum_1(lst):
    lst.remove(min(lst))
    return sum(lst)
print(max_sum_1([1, -2, 0, 3]))

# alternative
def max_sum_1(lst):
    lst.remove(sorted(lst)[0])
    return sum(lst)
print(max_sum_1([1, -2, 0, 3]))


# Write a function to check if given string is an palindrom
def is_palindrom(string):
    return string == string[::-1]
print(is_palindrom("abcba"))


# -----------------------------------Classes-------------------------------
# Person Class: Create a Python class called Person with attributes name and age. Implement a method to introduce the person.

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, my name is {self.name}. I am {self.age} years old."
    
filankes = Person(name='Ali', age='25')
print(filankes.introduce())

# Calculator Class:
# Define a class Calculator with methods for addition, subtraction, multiplication, and division.
class Calculator:
    @staticmethod
    def add(num1, num2):
        return num1 + num2
    @staticmethod
    def multiply(num1, num2):
        return num1 * num2
    @staticmethod
    def subtract(num1, num2):
        return num1 - num2
    @staticmethod
    def divide(num1, num2):
        return num1 / num2
    
print(Calculator.add(2,3))
print(Calculator.multiply(2,3))
print(Calculator.subtract(2,3))
print(Calculator.divide(2,3))

# alternative
class Calculator:
    def __init__(self) -> None:
        pass
    def add(self, num1, num2):
        return num1 + num2
    def multiply(self, num1, num2):
        return num1 * num2
    def subtract(self, num1, num2):
        return num1 - num2
    def divide(self, num1, num2):
        return num1 / num2
calc = Calculator()
print(calc.add(2,3))
print(calc.multiply(2,3))
print(calc.subtract(2,3))
print(calc.divide(2,3))


# Student Class: Design a class Student with attributes name, age, and grade. Implement a method to display student information.
class Student:
    def __init__(self, name:str, age:int, grade:int) -> None:
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student(name: {self.name}, age: {self.age}, grade: {self.grade})"
    
filankes = Student(name='Ali', age='25', grade=85)
print(filankes)

# #Given the below class:
# class Cat:
#     species = 'mammal'
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age

# 1 Instantiate the Cat object with 3 cats

class Cat():
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"({self.name}, {self.age})"

# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("mestan", 2)
cat2 = Cat("bella", 3)
cat3 = Cat("mila", 0)

# 2 Create a function that finds the oldest cat
def find_oldest_cat(list_of_cats):
    oldest_cat_age = 0
    oldest_cat = None
    for cat in list_of_cats:
        if cat.age > oldest_cat_age:
            oldest_cat_age = cat.age
            oldest_cat = cat
    return oldest_cat
print(find_oldest_cat([cat1,cat2,cat3]))

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in 2
oldest_cat = find_oldest_cat([cat1,cat2,cat3])
print(f"The oldest cat is {oldest_cat.age} years old.")


# alternative
class Cat():
    species = 'mammal'
    cat_instances = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.cat_instances.append(self)

    def __repr__(self):
        return f"({self.name}, {self.age})"
    
    @classmethod
    def find_oldest_cat(cls):
        oldest_cat = None
        oldest_cat_age = 0

        for cat in cls.cat_instances:
            if cat.age > oldest_cat_age:
                oldest_cat_age = cat.age
                oldest_cat = cat
        return oldest_cat

# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("mestan", 2)
cat2 = Cat("bella", 3)
cat3 = Cat("mila", 0)

print(Cat.find_oldest_cat())

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in 2
oldest_cat = Cat.find_oldest_cat()
print(f"The oldest cat is {oldest_cat.age} years old.")


# ---------------------------------lesson 7---------------------------------
# ---------------------------------Functional programming-------------------

# Implement a function that takes a list of numbers and returns a new list with each number squared
def sqr(n:int|float):
    return n**2
ans = map(sqr, [1,2,3,4,5])
print(list(ans))

# Write a function that transforms a list of strings to uppercase using the map function.
def to_upper(s:str):
    return s.upper()
ans = map(to_upper, ['salam', 'menim', 'adim', 'filankesdir'])
print(list(ans))

# Create a function that filters out even numbers from a list.
def is_odd(n:int):
    if n%2 == 0:
        return False
    else:
        return True
ans = filter(is_odd, [1,2,3,4,5,6])
print(list(ans))

# Write a function to filter words in a list that have more than 5 characters.
def is_big_word(s:str):
    return len(s) > 5
ans = filter(is_big_word, ['salam', 'menim', 'adim', 'filankesdir'])
print(list(ans))

# Implement a function that takes a list of numbers and returns a new list with only the positive numbers.
def is_positive(n:int|float):
    return n > 0
ans = filter(is_positive, [1.1,2,-3,-4.5,5.0,6.93938])
print(list(ans))

# Anonymous Functions (Lambda):
# Use lambda functions to create a list of the squares of the numbers from 1 to 10.
ans = map(lambda n: n**2, range(1,11))
print(list(ans))

# Filter a list of words to include only those starting with a vowel using a lambda function.
ans = filter(lambda word: word[0].lower() in 'aouei', ['salam', 'menim', 'adim', 'filankesdir'])
print(list(ans))

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
ans = map(lambda word: word.capitalize(), my_pets)
print(list(ans))

#3 Filter the scores that pass over 50
scores = [73, 20, 65, 19, 76, 100, 88]
ans = filter(lambda n: n > 50, scores)
print(list(ans))
