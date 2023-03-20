"""
Question 31:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

"""

def genDict():
    return {i: i**2 for i in range(0,21)}  # List comprehension to find the square of each key

print(genDict())


"""
Question 32:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

"""

def genKeys():
    return {i: i**2 for i in range(0,21)}  # List comprehension to find the square of each key

print(genKeys().keys())                    # keys() method is used to print all the keys


"""
Question 33:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

"""

def genList():
    return [i**2 for i in range(0,21)]  # List comprehension to find the square of each key and print values

print(genList())


"""
Question 34:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

"""

def genListOfFive():
    return [i**2 for i in range(0,21)][:5]  # List comprehension to find the square of each key and printing first 5 elements

print(genListOfFive())


"""
Question 35:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

"""

def genListOfLastFive():
    return [i**2 for i in range(0,21)][-5:]  # List comprehension to find the square of each key and printing last 5 elements

print(genListOfLastFive())


"""
Question 36:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

"""

def genListExceptFirstFive():
    return [i**2 for i in range(0,21)][5:]  # List comprehension to find the square of each key and printing all elements except first 5 elements as index starts from 0 and not 1

print(genListExceptFirstFive())


"""
Question 37:
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

"""

def genTuple():
    return tuple((i**2 for i in range(0,21)))  # List comprehension to find the square of each key and printing all elements except first 5 elements as index starts from 0 and not 1

print(genTuple())