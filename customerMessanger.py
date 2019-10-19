import datetime

userInfoDatabase = {}
allMessagesDB = {}
currentUserInfo = []

class setUsers:


    def __init__(self):
        self.surnName = input("Surnname: ")
        self.firstName = input("First Name: ")
        self.name = ""
        self.email = input("Email Address: ")
        self.itemBought = input("Item Bought: ")
        self.itemAmount = float(input("Amount (NGN): "))
        yyyy = int(input("Date\n\tYYYY: "))
        mm = int(input("\tMM: "))
        dd = int(input("\tDD: "))
        self.date = datetime.date(yyyy,mm,dd)
        self.message = ""

    def formatInformation(self):
        self.surnName = self.surnName[0].upper() + self.surnName[1:].lower()
        self.firstName = self.firstName[0].upper() + self.firstName[1:].lower()
        self.itemBought = self.itemBought[0].upper() + self.itemBought[1:].lower()
        self.name = self.surnName +" "+ self.firstName
        self.itemAmount = "NGN" + str(self.itemAmount)
        currentUserInfo.append(self.name)
        currentUserInfo.append(self.email)
        currentUserInfo.append(self.itemBought)
        currentUserInfo.append(self.itemAmount)
        currentUserInfo.append(self.date)
        return

    def setMessage(self):
        self.message = "\n\nTo: {0}\nDear {1},\n\nWe hope this message meets you in good time, we will like to use this medium to express our gratitude towards your patronage on {2} when you bought {3} for {4} from Softwareshop Limited.\n\nBest Regards!\nSoftwareshop Limited\n\n".format(self.email, self.name, self.date, self.itemBought, self.itemAmount)

        currentUserInfo.append(self.message)
        allMessagesDB[self.name] = self.message
        return

    def addUser(self):
        userInfoDatabase[self.name] = currentUserInfo
        print("\tUser Added\n\n")
        nextthing = (input("\nEnter 1 to go to main menu or other buttons to exit\n>>>"))
        if (nextthing == "1"):
            return
        else:
            exit()

class getUserInfo():

    def printUserMssg(self, name):
        print(allMessagesDB[name])

        nextthing = (input("\nEnter 1 to go to main menu or other buttons to exit\n>>>"))
        if (nextthing == "1"):
            return
        else:
            exit()

    def printAllUserMssg(self):
        print(allMessagesDB)
        nextthing = (input("\nEnter 1 to go to main menu or other buttons to exit\n>>>"))
        if (nextthing == "1"):
            return
        else:
            exit()

    def printAllUserInfo(self):
        print(userInfoDatabase)
        nextthing = (input("\nEnter 1 to go to main menu or other buttons to exit\n>>>"))
        if (nextthing == "1"):
            return
        else:
            exit()

def main():
    while (0<1):

        print("********************************************\n\n CUSTOMER MESSENGER SOFTWARE.\n\n********************************************\n\nEnter the corresponding number to do any of the following;\n  1.    Add a new customer\n  2.    Print a user message\n  3.    Print all users information(no message)\n  4.    Print all users mssages\n\n" )



        option = int(input(">>> "))
        if(option == 1):
            newUser=setUsers()
            newUser.formatInformation()
            newUser.setMessage()
            newUser.addUser()
            print("\tUser Added\n")

        elif (option == 2):
            getInfo = getUserInfo()
            name = input("\n\nEnter the user's full name (Surnname Fullname): ")
            getInfo.printUserMssg(name)
            #call method to print specific user message

        elif (option ==3):
            getInfo = getUserInfo()
            getInfo.printAllUserInfo()

        else:
            if (option ==4):
                getInfo = getUserInfo()
                getInfo.printAllUserMssg()
                #call method to print all users messages


if __name__ == '__main__':
    main()
