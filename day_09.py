"""
Question 26:
Define a function which can compute the sum of two numbers.

"""

def sum(num1, num2):
    return num1 + num2

num1 = int(input("Enter the first number \n"))
num2 = int(input("Enter the second number \n"))
print(sum(num1,num2))

# Alternative method
# sum = lambda n1, n2: n1 + n2  # here lambda is use to define little function as sum
# print(sum(1, 2))


"""
Question 27:
Define a function that can convert a integer into a string and print it in console.

"""

def convertToString(val):
    return(str(val))

val = int(input("Enter the value to be converted into string \n"))
print("Type of value before converting to string is ", type(val))
val2 = convertToString(val)
print("Type of value after converting to string is ", type(val2))


"""
Question 28:
Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.

"""

sum = lambda s1, s2: int(s1) + int(s2)      # Type casting inside the lambda function
print(sum("10", "45"))  # 55


"""
Question 29:
Define a function that can accept two strings as input and concatenate them and then print it in console.

"""

def concatenate(str1, str2):
    return str1+str2

str1 = input("Enter first string \n")     # 10
str2 = input("Enter second string \n")    # 45
print(concatenate(str1, str2))            # 1045


"""
Question 30:
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

"""

def maxString(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str1) < len(str2):
        return str2
    else: return (str1 + "\n" + str2)

str1 = input("Enter first string \n")
str2 = input("Enter second string \n")
print(maxString(str1, str2))            # 10454