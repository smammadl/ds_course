# Python
# --------------------------------Variables---------------------------------
# Declare two variables, x and y, and assign them the values 5 and 10. Print their sum.

# Create a variable name and assign your name to it. Print a greeting using the variable.


# ----------------------------Conditional Statements-------------------------------
# Write a program that checks if a given number is even or odd.
num = 10

# Create a program that determines if a student's grade is 'A,' 'B,' 'C,' or 'Fail' based on their score.
score = 85

# Implement a calculator that performs addition, subtraction, multiplication, or division based on user input.
num1 = 10
num2 = 5
operator = "+"

# ----------------------------Loops---------------------------------
# Write a while loop that prints the square of numbers from 1 to 5.


# Implement a countdown timer using a while loop. Start from 10 and print the countdown value until reaching 1. 
# After reaching 1, print "Happy Birthday!"(only once)


# Write a program that prints numbers from 1 to 50. For multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz." 
# For numbers that are multiples of both 3 and 5, print "FizzBuzz."


# Write a program that gives you a total of numbers from 1 to 100 -  Answer: 5050


# Factorial Calculation:
# Implement a program to calculate the factorial of the number  5 using a for loop.
# Answer 120


# Even Numbers:
# Write a program to print all even numbers between 1 and 20 using a while loop and if condition.


# Pattern Printing:
# Create a program to print the following pattern using loops:

#
##
###
####
#####


# Create a program to print the following pattern using loops:

#####
####
###
##
#


# Create a program to print the following pattern using loops:

#     *
#    ***
#   *****
#  *******

# ----------------------------Tuples---------------------------------
# Create a tuple with three integers. Find the sum of the elements.
my_tuple = (1, 2, 3)

# Find the highest number from a list
my_list = [1, 2, 3, 4]

# Find the second-highest number from a list
my_list = [4, -3,-2,1,1,4]

# Find the second (distinct) highest number from a list
my_list = [4, -3,-2,1,1,4]

# Define a dictionary with keys 'name', 'age', and 'city'. Print the values.
my_dict = {"name": "Ali", "age": 20, "city": "Baku"}

# Write a program to print all odd numbers backward from 15 to 1 using a for loop.

# ----------------------------Functions---------------------------------

# Even or Odd Function:
# Write a Python function that takes an integer as input and returns "Even" if it's even and "Odd" if it's odd.
def even_or_odd(num):
    pass

# Factorial Function:
# Implement a function to calculate the factorial of a given number.
def factorial(num):
    pass

# Build a simple guessing game:
# The game should generate a random number between 1 and 10 and ask the user to guess it.
# If the guess is correct, the game should print "You won!" and exit.
# If the guess is incorrect, the game should print "Try again" and ask the user to guess again.
pass

# Add two new functionalities to this game:
# The game should give you hints when your guess is wrong. 
pass

# Add a new functionality to this game:
# You should only have three chances to guess the number
pass

# count vowels in the string "Hello World"
def count_vowels(string):
    pass

# sum of digits of the number 12345
def sum_of_digits(n):
    pass

# find primes in the range [10, 20]
def find_primes_in_range(start, end):
    pass

# find the length of the longest word in the sentence "The quick brown fox jumps over the lazy dog"
def longest_word_length(sentence):
    pass

# calculate the nth fibonacci number
def fibonacci(n):
    pass


# remove duplicates from the list [1, 2, 2, 3, 4, 4, 5]
def remove_duplicates(lst):
    pass


# --- find_anagrams("listen", ["enlist", "google", "inlets", "banana"])
def find_anagrams(word, words):
    pass


# check if the number is a perfect square
def is_perfect_square(n):
    pass


# find the longest substring with unique letters in the string "abcdpabcbb"
def longest_unique_substring(string):
    pass

# rotate_list([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
def rotate_list(lst, n):
    pass

# check if the list is sorted [1, 2, 3, 4, 5]
def is_sorted(arr): 
    pass

# count frequency of elements in the list [1, 2, 2, 3, 3, 3, 4]
def count_frequency(lst):
   pass


# implement bubble sort algorithm for the list [64, 34, 25, 12, 22, 11, 90]  
# link: https://en.wikipedia.org/wiki/Bubble_sort
def bubble_sort(arr):
    pass

# Input: [1, -2, 0, 3]
# Output: 4
# Explanation: We can delete only one element and obtain the maximum sum of 4
def max_sum_1(lst):
    pass

# Write a function to check if given string is an palindrom
def is_palindrom(string):
    pass

# -----------------------------------Classes-------------------------------
# Person Class: 
# Create a Python class called Person with attributes name and age. 
# Implement a method to introduce the person.

class Person:
    pass

# Calculator Class:
# Define a class Calculator with methods for addition, subtraction, multiplication, and division.
class Calculator:
    pass

# Student Class: 
# Design a class Student with attributes name, age, and grade. 
# Implement a method to display student information.
class Student:
    pass

# #Given the below class:
# class Cat:
#     species = 'mammal'
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age

# 1 Instantiate the Cat object with 3 cats

# 2 Create a function that finds the oldest cat

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in 2

# ---------------------------------Functional programming-------------------

# Implement a function that takes a list of numbers and returns a new list with each number squared
def sqr(n:int|float):
    pass

# Write a function that transforms a list of strings to uppercase using the map function.
def to_upper(s:str):
    pass

# Create a function that filters out even numbers from a list.
def is_odd(n:int):
    pass

# Write a function to filter words in a list that have more than 5 characters.
def is_big_word(s:str):
    pass

# Implement a function that takes a list of numbers and returns a new list with only the positive numbers.
def is_positive(n:int|float):
    pass

# Anonymous Functions (Lambda):
# Use lambda functions to create a list of the squares of the numbers from 1 to 10.

# Filter a list of words to include only those starting with a vowel using a lambda function.

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

#3 Filter the scores that pass over 50
scores = [73, 20, 65, 19, 76, 100, 88]
