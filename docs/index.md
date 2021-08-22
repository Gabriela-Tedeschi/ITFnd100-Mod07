# Pickling & Structured Error Handling Demonstrations  
**Dev:** *Gabriela Tedeschi*  
**Date:** *8/22/2021*  

## Introduction  
In this document, I will describe the steps I took to write a script that demonstrates how pickling and structured error handling are used in the Python language. For pickling, I created one large demo that uses functions to separate concerns and that performs a practical task. For error handling, while I concerned taking the same approach, I chose to write several unconnected examples to demonstrate the different techniques we learned in a simple way.  

## Pickling  
I started this demo by simply declaring two variables I would need, one to store the file name and a list that would store the data. (While I’m not sure if it’s a best practice, I only declared the variables that exist outside of functions as this felt most helpful for planning purposes.) Then I created a Processing section, declaring two functions in the class Processor. For the writing function, I added a doc string, used the open function to open a file, used “ab”, which gives the command to write to the file in binary, and used the pickle.dump function to write the contents of the lst parameter to the file. At the end, a message to the user is returned.  

For the reading function, I chose “rb” for the open function, which gives the command to read binary from the file. I then declared an empty list and use the pickle.load function to put the contents of the file into the list. At the end, the function returns the lst parameter.

![Pickling Functions](https://github.com/Gabriela-Tedeschi/ITFnd100-Mod07/blob/main/docs/pickling%20functions.png "Pickling Functions")  

In the demo section, I printed some messages to the user to let them know what I was trying to demonstrate. Then, I assigned some items to the list, todo_lst. I then passed this variable and the variable storing the file name as arguments into the writing function I created. This is within a print function, so it prints the function’s return message to the user, which lets them know they wrote to the file successfully.  

I then emptied todo_lst, called the reading function, and assigned the list the function returns to todo_lst, so the contents of the file are stored in todo_lst. Then, I printed todo_lst. Because the list variable was emptied before the read function ran, the user knows that the contents of the file were read and assigned to the list successfully.

![Pickling Demo](https://github.com/Gabriela-Tedeschi/ITFnd100-Mod07/blob/main/docs/pickling%20demo.png "Pickling Demo")  

## Structured Error Handling  
The first two examples I created in Structured Error Handling Demos section simply use the general Exception class and provide both custom, easy-to-understand error messages that I wrote and Python’s built-in error info. The first example triggers a FileNotFoundError, while the second triggers a ZeroDivisionError.  

```
try:
    objFile = open('fake_file.txt', "r")
    objFile.close()

except Exception as e:
    print('Text file does not exist! Please double check the name you entered.')
    print('Built-In Python error info: ')
    print(e, e.__doc__, type(e), sep='\n')  # Will print the error's description, doc string, and class
print()
```  
```
try:
    quotient = 3/0

except Exception as e:
    print('Cannot divide by zero!')
    print('Built-In Python error info: ')
    print(e, e.__doc__, type(e), sep='\n')
input()
```  

In the next subsection, I demonstrate how to use specific Exception classes – FileNotFoundError and ZeroDivisionError, the same two that I returned with my previous examples. To do this, I name these specific classes in my except statements and “e” stores the class information just as it does with the Exception class. I chose to create two examples with the same two except blocks and try blocks that are identical, except that the code comes in a different order. (The division by zero error comes first in one and the file not found error comes first in the other.) This allows the user to observe that only the first error will be caught and that this determines which class’s info will be returned.  

```
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
```  

For the Custom Errors subsection, I demonstrate that you can raise custom errors by setting a custom condition as an if statement in the try block. I set a condition that the string must be 5 or fewer characters long. As my string is longer than this, the except block returns both the custom messages I wrote and Python’s info. Note that the message I provided in the raise Exception statement is stored in “e”.  

```
try:
    string = 'abcdef'
    if len(string) > 5:
        raise Exception('Please use a string with 5 or fewer characters.')

except Exception as e:
    print('The string length raises a custom error.')
    print('Built-In Python error info: ')
    print(e, e.__doc__, type(e), sep='\n')
input()
```

In the final example, I demonstrate how to create custom Exception classes. I created two classes, added doc strings, and defined functions within them – one that gives a message about the max acceptable length of a string and one that gives a message about the minimum acceptable length of string.  

I use these functions in the try block in a way that’s similar to the example above. Instead of using a raise Exception statement, I use the raise keyword with the names of the functions I created. Based on the conditional statements I used, one of these functions will be raised and its info will be stored in “e”. In this case, I used a string that is too short, so the information that prints is about the minimum string length error.  

```
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
```  

## Running The Program  
The images below show the program running in PyCharm and the command shell:  

### PyCharm  
![Program running in PyCharm, part 1](https://github.com/Gabriela-Tedeschi/ITFnd100-Mod07/blob/main/docs/PyCharm%201.png "Program running in PyCharm, part 1")  
![Program running in PyCharm, part 2](https://github.com/Gabriela-Tedeschi/ITFnd100-Mod07/blob/main/docs/PyCharm%202.png "Program running in PyCharm, part 2")  

### Command Shell
![Program running in command shell, part 1](https://github.com/Gabriela-Tedeschi/ITFnd100-Mod07/blob/main/docs/command%201.png "Program running in command shell, part 1")
![Program running in command shell, part 2](https://github.com/Gabriela-Tedeschi/ITFnd100-Mod07/blob/main/docs/command%202.png "Program running in command shell, part 2")  

## Summary  
In this document, I discussed the steps I took to create pickling and structured error handling demos. In the process, I gave an overview of how functions related to pickling and error handling work and the different options that these functions provide.






