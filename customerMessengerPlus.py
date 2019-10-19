import datetime
import smtplib


host = "smtp.gmail.com"
port = 587
username = "ishaqmuhammed191@gmail.com"
to_email="ishaqmuhammed191@gmail.com"


userInfoDatabase = {}
allMessagesDB = {}



class setUsers:

    def __init__(self):
        self.surnName = input("Surnname: ")
        self.firstName = input("First Name: ")
        self.name = ""
        self.email = input("Email Address*: ")
        self.itemBought = input("Item Bought: ")
        self.itemAmount = input("Amount (NGN): ")
        yyyy = int(input("Date\n\tYYYY: "))
        mm = int(input("\tMM: "))
        dd = int(input("\tDD: "))
        self.date = datetime.date(yyyy,mm,dd)
        self.message = ""
        self.data = {}

    def formatInformation(self):
        self.surnName = self.surnName[0].upper() + self.surnName[1:].lower()
        self.firstName = self.firstName[0].upper() + self.firstName[1:].lower()
        self.itemBought = self.itemBought[0].upper() + self.itemBought[1:].lower()
        self.name = self.surnName +" "+ self.firstName
        self.itemAmount = "NGN" + str(self.itemAmount)

        self.data.update({'name':self.name})
        self.data.update({'email':self.email})
        self.data.update({'itemBought':self.itemBought})
        self.data.update({'itemAmount':self.itemAmount})
        self.data.update({'purchaseDate':self.date})
        return

    def setMessage(self):
        self.message = "\n\nDear {0},\n\nWe hope this message meets you in good time, we will like to use this medium to express our gratitude towards your patronage on {1} when you bought {2} for {3} from Softwareshop Limited.\n\nBest Regards!\nSoftwareshop Limited\n\n".format(self.name, self.date, self.itemBought, self.itemAmount)

        self.data.update({'message':self.message})
        allMessagesDB.update({self.name:self.message})
        return

    def addUser(self):
        userInfoDatabase.update({self.name:self.data})
        print("\n\nUser Added\n\n")
        nextthing = (input("\nEnter 1 to go to main menu or other buttons to exit\n\n>>>"))
        if (nextthing == "1"):
            return
        else:
            exit()



class getUserInfo():

    def printUserMssg(self, name):
        print(allMessagesDB[name])

        nextthing = (input("\nEnter 1 to go to main menu or other buttons to exit\n\n>>>"))
        if (nextthing == "1"):
            return
        else:
            exit()

    def printAllUserMssg(self):
        print(allMessagesDB)
        nextthing = (input("\nEnter 1 to go to main menu or other buttons to exit\n\n>>>"))
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



class sendMessage():

    def messageAllCustomers(self):

        try:
            if (len(userInfoDatabase) > 0):
                email_conn = smtplib.SMTP(host,port)
                email_conn.ehlo()
                email_conn.starttls()
                password = input("Enter your gmail password: ")
                email_conn.login(username, password)
                for details in userInfoDatabase:
                    user_message = userInfoDatabase[details]['message']
                    user_email = userInfoDatabase[details]['email']
                    email_conn.sendmail(username, user_email, user_message)
                print("\n\n>>> Sent!")
            else:
                print(">>> No data in database <<<\n")
                return

        except:
            print("error sending message")



def main():
    while (0<1):

        print("********************************************\n\n CUSTOMER MESSENGER SOFTWARE.\n\n********************************************\n\nEnter the corresponding number to do any of the following;\n  1.    Add a new customer\n  2.    Print a user message\n  3.    Print all users information(no message)\n  4.    Print all users mssages\n  5.    Send mail to all customers\n  6.    Quit\n\n" )

        try:
            option = int(input(">>> "))
            if (option == 1):
                newUser=setUsers()
                newUser.formatInformation()
                newUser.setMessage()
                newUser.addUser()
                #print("\tUser Added\n")

            elif (option == 2):
                getInfo = getUserInfo()
                name = input("\n\nEnter the user's full name (Surnname Fullname): ")
                getInfo.printUserMssg(name)
                #call method to print specific user message

            elif (option == 3):
                getInfo = getUserInfo()
                getInfo.printAllUserInfo()

            elif (option == 4):
                getInfo = getUserInfo()
                getInfo.printAllUserMssg()

            elif (option == 5):
                messageSender = sendMessage()
                messageSender.messageAllCustomers()

            elif (option == 6):
                break
                exit()

        except:
            print(">>>>> Wrong value inputed <<<<<\n")


if __name__ == '__main__':
    main()
