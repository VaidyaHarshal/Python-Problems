"""
Question 4:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program: 34,67,55,33,12,98

Then, the output should be:
['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.tuple() method can convert list to tuple

"""

# By default the input method stores the value as string so the split method is available
lst = input("Enter the comma seperated values to be converted into list and tuples \n").split(',')
# Get the comma seperated input from user and split method splits the input and stores it as a list
tupl = tuple(lst)               # Convert the input into tuple
print(lst)
print(tupl)


"""
Question 5:
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
_Use init** method to construct some parameters_**

"""


class demoString:
    def __init__(self):                             # Constructor method to initialize variables
        pass

    def getString(self):                            # Get string method for getting an input string from user
        self.str = input("Enter the string \n")     # Taking input string from the user

    def printString(self):                          # Print string method for printing the input string from user
        print(self.str.upper())                     # upper method to convert string into uppercase

val = demoString()                                  # Creating an object of the class
val.getString()                                     # Calling the method getString which is present inside the class with the help of class object
val.printString()                                   # Calling the method printString which is present inside the class with the help of class object


"""
Question 6:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C and H:
C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:
100,150,180

The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26).In case of input data being supplied to the question, it should be assumed to be a console input.

"""
def calculate_val(numList):
    len_val = len(numList)                                                       # Finding the length of the input list
    final_array = []                                                             # Initializing the list
    for i in range(0, len_val):
        final_val = round(((2 * 50 * int(numList[i]))/30) ** 0.5)                # Storing the rounded values into a variable
        final_array.append(final_val)                                            # Appending the rounded values into an array

    D = [str(i) for i in final_array]                                            # Converting the integers into string to apply the join method for printing comma seperated values
    print(",".join(D))                                                           # Printing the values in a comma seperated way using join method

input_str = input("Enter the numbers in a comma seperated way \n").split(',')    # Taking input values from the user
calculate_val(input_str)                                                         # Calling the calculate function


"""
Question 7:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i * j.

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], 
 [0, 1, 2, 3, 4], 
 [0, 2, 4, 6, 8]]

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

"""

def gen_matrix(numList):
    lst = []                                                                                # Initializing the list
    x, y = map(int, numList)                                                                # Splitting the dimensions into the variables x and y
    for i in range(x):                                                                      # i represents the row of the matrix
        temp = []
        for j in range(y):                                                                  # j represents the column of the matrix
            temp.append(i * j)                                                              # Storing the values row wise in temporary array
        lst.append(temp)                                                                    # Appending the values into the main list
    print(lst)

values = input("Enter the comma seperated values for the matrix dimension \n").split(",")   # Taking matrix dimensions from the user
gen_matrix(values)                                                                          # Calling the function


"""
Question 8:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world

Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

char_list = input("Enter the words in a comma seperated way \n").split(',')      # Taking input words from user in a comma seperated way
char_list.sort()                                                                 # Using the sort method to sort the list elements
print(",".join(char_list))                                                       # Printing the values in a comma seperated way using join method 


"""
Question 9:
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:
Hello world
Practice makes perfect

Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

lst = []
while True:                                 # While loop to be executed atleast once
    x = input("Enter the words \n")         # Taking input words from user in a comma seperated way
    if len(x) == 0:                         # Condition to check if user has entered any value
        break
    lst.append(x.upper())                   # Appending the upper case value into the list

for val in lst:
    print(val)                              # To print the values of the list