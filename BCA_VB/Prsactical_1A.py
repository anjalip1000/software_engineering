''' 1.	Create a program that asks user to enter their name and their age.
Print out a message addressed to them that tells them the
year that they will turn 100 years old.
'''

def practical_one():
    name = input("Please enter your name:  ")
    age = int(input("Please enter your age:  "))
    print("Hi {}, after 100 years, you will be {} old.".format(name, age + 100))
    return


practical_one()