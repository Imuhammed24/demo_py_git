#a program that accepts a number, pass it to a method and output the result

number = int(input('Enter a number: '))

def addtwentyfive(x): #tis could be def addtwentyfive(x=0)
    x+=25
#return x
    print(x)
#you can use return statement instead of print if you wont like to print out the end result on screen.

#number2 = 10 + addtwentyfive(number)
#print(number2)

#the code below will help us run the method, and a value will be outputed based on the print statement in the function.
addtwentyfive(number)
