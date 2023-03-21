"""
Question 38:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

"""

def printTuple(tupl1):
    length = int(len(tupl1)/2)          # Finding the mid point of the tuple by dividing length of tuple by 2
    print(tupl1[:length])
    print(tupl1[length:])
    #return (tupl1[:length], tupl1[length:])

tupl1 = (1,2,3,4,5,6,7,8,9,10)
printTuple(tupl1)


"""
Question 39:
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

"""

def evenTuple(tupl1):
    tupl2 = (i for i in tupl1 if i % 2 == 0)       # Finding values which are divisible by 2
    return tuple(tupl2)

tupl1 = (1,2,3,4,5,6,7,8,9,10)
print(evenTuple(tupl1))


"""
Question 40:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

"""

def printString(str1):
    if str1 == "yes" or str1 == "YES" or str1 == "Yes":
        return "Yes"
    else:
        return "No"

str1 = "YES"
print(printString(str1))


"""
Question 41:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

"""

def mapList(num):
    return num**2

lst1 = [1,2,3,4,5,6,7,8,9,10]
result = map(mapList,lst1)
print(list(result))

# result = map(lambda x: x ** 2, li)  # Using Lambda, returns map type object data
# print(list(result))


"""
Question:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

"""

lst1 = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = list(filter(lambda x: x % 2 == 0, lst1))
result = map(lambda x: x**2, evenNumbers)
print(list(result))


"""
Question 43:
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

"""

lst1 = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = list(filter(lambda x: x % 2 == 0, lst1))
print(list(evenNumbers))