"""
uname = input('Please Enter Your Name: ')
uage = int(input('Enter Your Age: '))

if (uage <18) and (uage!=0):
    print('Sorry {0}, you are less than 18 years old'.format(uname))
elif uage >18 or uage==18:
    print('Welcome Mr {0}, you are above 18 years.'.format(uname))
else:
    if uage == 0:
        print('Invalid Age')
"""





"""
# a basic for loop
i = 2
#eqivalent to 'for each index in range(0-10)'
for allNumbers in range(11):
#the variable numbers stands 4 d value of the current index of the loop.
    print(i**allNumbers)

    #i = i+2
"""





"""
#A program that allows users to enter 10 names into a list

tenNames = ['a','b','c','d','e','f','s','w','q','z']

for names in range(10):
    submittedNames = input('please enter 10 Names: ')
    tenNames[names] =submittedNames
#prining the list with each element on a newline with the cmd below
print(*tenNames, sep='\n')
"""



# a program that accepts x numbers and prints them. You can also sort it and slice it to print the top highest/lowest.
scores = []
i = 0

numOfScore = int(input('Please Enter the amount of scores you want to input:\n'))
print('Please Enter {0} scores\n'.format(numOfScore))
for numbers in range(numOfScore):
    item = int(input())
    scores.insert(i, item)
    i+=1

#scores.sort()
print("\nYou just entered the following scores\n", *scores, sep='\n')
