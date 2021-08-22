# Pickling & Structured Error Handling Demonstrations  
**Dev:** *Gabriela Tedeschi*  
**Date:** *8/22/2021*  

## Introduction  
In this document, I will describe the steps I took to write a script that demonstrates how pickling and structured error handling are used in the Python language. For pickling, I created one large demo that uses functions to separate concerns and that performs a practical task. For error handling, while I concerned taking the same approach, I chose to write several unconnected examples to demonstrate the different techniques we learned in a simple way.  

## Pickling  
I started this demo by simply declaring two variables I would need, one to store the file name and a list that would store the data. (While I’m not sure if it’s a best practice, I only declared the variables that exist outside of functions as this felt most helpful for planning purposes.) Then I created a Processing section, declaring two functions in the class Processor. For the writing function, I added a doc string, used the open function to open a file, used “ab”, which gives the command to write to the file in binary, and used the pickle.dump function to write the contents of the lst parameter to the file. At the end, a message to the user is returned.  

For the reading function, I chose “rb” for the open function, which gives the command to read binary from the file. I then declared an empty list and use the pickle.load function to put the contents of the file into the list. At the end, the function returns the lst parameter.

