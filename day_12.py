"""
Question 44:
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

"""

newList = list(map(lambda x: x**2, range(0,21)))
print(newList)


"""
Question 45:
Define a class named American which has a static method called printNationality.

"""

class American:
    @staticmethod                   # Used to decorate the static method
    def nationality():
        natl = "I am Indian"
        print(natl)
    
amr = American()
amr.nationality()
American.nationality()
    

"""
Question 46:
Define a class named American and its subclass NewYorker.

"""

class American:
    pass

class NewYorker(American):
    pass

american = American()
newyorker = NewYorker()

print(american)
print(newyorker)