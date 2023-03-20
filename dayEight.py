"""
Question 22:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

"""

inputStr = input("Enter a string to find the frequency of words \n").split()
sortedStr = sorted(inputStr)                                # Sort the input list

for i in sortedStr:
    print("{0}:{1}".format(i,sortedStr.count(i)))           # Print the list according to the format with {0} as key and {1} as count

#from pprint import pprint
#inputStr = input("Enter a string to find the frequency of words \n").split()
#print(inputStr)
#pprint({i:inputStr.count(i) for i in inputStr})


"""
Question 23:
Write a method which can calculate square value of number

"""

def squareVal(num):
    return num**2

num = int(input("Enter a number to find the square \n"))
print(squareVal(num))


"""
Question 24:
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function

Hints:
The built-in document method is doc

"""

def pow(n, p):
    return n**p

print(str.__doc__)
print(sorted.__doc__)
print(pow(3,4))
print(pow.__doc__)


"""
Question 25:
Define a class, which have a class parameter and have a same instance parameter.

"""

class Car:
    name = 'Car'

    def __init__(self, name=None):
        self.name = name

honda = Car('Honda')                            # Passing the name of the car in the arguement for the instance of the object honda 
print(f"{Car.name} name is {honda.name}")       # Car.name is the class variable and honda.name is the object variable

toyota = Car()                                  # Creating a class object
toyota.name = 'Toyota'                          # Setting the object name to Toyota
print(f"{Car.name} name is {toyota.name}")      # Car.name is the class variable and toyota.name is the object variable