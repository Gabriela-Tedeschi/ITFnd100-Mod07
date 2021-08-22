# ------------------------
# Title: Assignment 07
# Description: Demonstrates how pickling and structured error handling work
# ChangeLog (Who, When, What):
# G Tedeschi, 8/21/2021, Created script
# ------------------------

# ----- Pickling Demo ----- #

# Data

filename1 = 'ToDoList.txt'
todo_lst = []

# Processing

import pickle

class Processor:
    """ Performs processing tasks """

    @staticmethod
    def write_data_to_file_binary(file, lst):
        """ Writes list to file in binary

        :param file: (string) name of file you want to write to
        :param lst: (list) you want to write to the file
        :return:nothing
        """
        objFile = open(file, "ab")
        pickle.dump(lst, objFile)
        objFile.close()
        return 'Data successfully written to file!'

    @staticmethod
    def read_data_from_binary_file(file):
        """ Reads data from file in binary format

        :param file: (string) name of file you want to write to
        :param lst: (list) you want to write to the file
        :return:lst
        """
        objFile = open(file, "rb")
        lst = []
        lst = pickle.load(objFile)
        objFile.close()
        return lst

# Pickling Demo

print('---Pickling Demo---')
print('The first function called below will write the contents of todo_lst to a file in binary format.')
print('The second function called below will read from the file and print the contents.')
input('Press enter to continue.')
print() # Add extra line for readability

todo_lst = ['Vacuum', 'Dishes', 'Homework']
print(Processor.write_data_to_file_binary(filename1, todo_lst))
print()

todo_lst = []
todo_lst = Processor.read_data_from_binary_file(filename1)
print(todo_lst)
print()

input('Press enter to continue to the error handling demos.')
print()

# ----- Structured Error Handling Demos ----- #

# Using The Exception Class

print('---Structured Error Handling Demos---')
print('This example demonstrates an attempt to open a file that does not exist.')
print()

try:
    objFile = open('fake_file.txt', "r")
    objFile.close()

except Exception as e:
    print('Text file does not exist! Please double check the name you entered.')
    print('Built-In Python error info: ')
    print(e, e.__doc__, type(e), sep='\n')  # Will print the error's description, doc string, and class
print()

input('Press enter after each example to continue.')
print()

print('This demonstrates an attempt to divide by zero.')
print()

try:
    quotient = 3/0

except Exception as e:
    print('Cannot divide by zero!')
    print('Built-In Python error info: ')
    print(e, e.__doc__, type(e), sep='\n')
input()

# Using Specific Exception Classes

print('The Exception class can catch any type of error.')
print('However, you can use more specific exception classes.')
print('In the two examples below, note that only the first error in the try statements will be caught.')
print()

try:
    quotient = 3/0
    objFile = open('fake_file.txt', "r")
    objFile.readline()
    objFile.close()

except ZeroDivisionError as e:  # Returns this (division by zero error is caught)
    print('Cannot divide by zero!')
    print('Built-In Python error info: ')
    print(e, e.__doc__, type(e), sep='\n')

except FileNotFoundError as e:
    print('Text file does not exist! Please double check the name you entered.')
    print('Built-In Python error info: ')
    print(e, e.__doc__, type(e), sep='\n')
input()

try:
    objFile = open('fake_file.txt', "r")
    objFile.readline()
    objFile.close()
    quotient = 3/0

except ZeroDivisionError as e:
    print('Please do no use zero!')
    print('Built-In Python error info: ')
    print(e, e.__doc__, type(e), sep='\n')

except FileNotFoundError as e:  # Returns this (file error is caught)
    print('File does not exist! Please double check the name you entered.')
    print('Built-In Python error info: ')
    print(e, e.__doc__, type(e), sep='\n')
input()

# Custom Errors

print('You can raise a custom error by setting a custom condition in the try block.')
print()
try:
    string = 'abcdef'
    if len(string) > 5:
        raise Exception('Please use a string with 5 or fewer characters.')

except Exception as e:
    print('The string length raises a custom error.')
    print('Built-In Python error info: ')
    print(e, e.__doc__, type(e), sep='\n')
input()

# Custom Exception Classes

print('You can also create custom classes that use the Exception class as a base.')
print('Doing this allows you to put a custom message in the class\'s doc string.')
print()

class MaxStringLength(Exception):
    """ The string must be 5 or fewer characters """
    def __str__(self):
        return 'String longer than 5 characters'

class MinStringLength(Exception):
    """  The string must be more than 1 character  """
    def __str__(self):
        return 'String less than 2 characters'

try:
    string = 'a'
    if len(string) == 1 or len(string) == 0:
        raise MinStringLength()
    elif len(string) > 5:
        raise MaxStringLength()

except Exception as e:
    print('There was a non-specific error!')
    print('Built-in Python error info:')
    print(e, e.__doc__, type(e), sep='\n')




