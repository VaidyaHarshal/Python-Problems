""" 
Question 1:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

for i in range(2000,3201):         # For the range of i between the numbers 2000 and 3201
    if i % 7 == 0 and i % 5 != 0:  # Check whether i is divisible by 7 and i is not divisible by 5
        print(i, end=',')          # Printing the numbers in a comma seperated format
print("\b")

""" 
Question 2:
Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""

def find_factorial(num):
    fact = 1                    # Initializing the fact value
    while num > 1:              # Loop runs till num value is greater than 1
        fact = fact * num       # Multiplying the fact value with each digit in the decreasing order of value num
        num -= 1                # Decreasing the value of num
    print(fact)
print(f"Enter the value to find the factorial")
num = int(input())              # Taking input value from the user
find_factorial(num)             # Calling the factorial function and passing the input value

""" 
Question 3:
With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8 Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

def gen_dict(val):
    ans = {}                    # Initializing the object
    for i in range(1, val+1):   # For the value range of 1 till val + 1 
        ans[i] = i * i          # Setting the value into object for the key of i
    print(ans)
print(f"Enter the number of values to be entered into dictionary")
val = int(input())              # Taking input value from the user
gen_dict(val)                   # Calling the gen_dict function and passing the input value