"""
Question 20:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use class, function and comprehension.

"""

class iterNum:
    def __init__(self):
        pass

    def checkDivisible(self, num):
        lst = [i for i in range(0, num+1) if i % 7 == 0]        # List comprehenstion to check if i is divisible by 7
        return lst

checkNum = int(input("Enter the number to check the divisibity from range 0 to n \n"))
divNum = iterNum()
lstNum = divNum.checkDivisible(checkNum)
print(lstNum)


"""
Question:
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.Here distance indicates to euclidean distance.Import math module to use sqrt function.

"""

#from math import dist
#tupl1 = input("Input the number of UP and DOWN steps taken by the Robot using a comma \n").split(",")
#tupl1 = tuple(map(int,tupl1))
#tupl2 = input("Input the number of LEFT and RIGHT steps taken by the Robot using a comma \n").split(",")
#tupl2 = tuple(map(int,tupl2))
#print(round(dist(tupl1,tupl2)))


from math import sqrt

x, y = 0, 0
while True:
    s = input("Enter the number of Steps taken by the Robot using UP/DOWN/LEFT/RIGHT \n").lower().split()
    if not s:
        break
    if s[0] == "up":            # s[0] indicates command
        x -= int(s[1])          # s[1] indicates unit of move
    if s[0] == "down":
        x += int(s[1])
    if s[0] == "left":
        y -= int(s[1])
    if s[0] == "right":
        y += int(s[1])
        # N**P means N^P
dist = round(sqrt(x ** 2 + y ** 2))  # Euclidean distance = square root of (x^2+y^2) and rounding it to nearest integer
print(dist)