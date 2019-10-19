import datetime
import smtplib


host = "mail.cvhub4africa.com"
port = 465
username = "joy@cvhub4africa.com"
to_email="joy@cvhub4africa.com"


userInfoDatabase = {}
allMessagesDB = {}



class setUsers:

    def __init__(self):
        self.name = input("Name: ")
        #self.firstName = input("First Name: ")
        #self.name = ""
        self.email = input("Email Address*: ")
        self.address = ""
        self.street_info = input("Address\n\tStreet Info: ")
        self.city_info = input("\tCity Info(e.g. GRA, Ikeja): ")
        self.state_info = input("\tState Info(e.g. Lagos, NG): ")
        #self.itemAmount = input("Amount (NGN): ")
        yyyy = int(input("Date\n\tYYYY: "))
        mm = int(input("\tMM: "))
        dd = int(input("\tDD: "))
        self.date = datetime.date(yyyy,mm,dd)
        self.message = ""
        self.data = {}

    def formatInformation(self):
        self.name = self.name.upper()
        self.address = self.street_info + ",\n" + self.city_info + ",\n" + self.state_info
        #self.firstName = self.firstName[0].upper() + self.firstName[1:].lower()
        #self.address = self.itemBought[0].upper() + self.itemBought[1:].lower()
        #self.name = self.surnName +" "+ self.firstName
        #self.itemAmount = "NGN" + str(self.itemAmount)
        self.data.update({'address':self.address})
        self.data.update({'name':self.name})
        self.data.update({'email':self.email})
        #self.data.update({'itemBought':self.itemBought})
        #self.data.update({'itemAmount':self.itemAmount})
        self.data.update({'date':self.date})
        return

    def setMessage(self):
        self.message = "{0}\n\n{1}\n\nDear Sir/ma,\nSoftwareshop Limited, founded in 2003 and headquartered in Ikeja, with a branch fully registered in South-Africa as Softwareshop (PTY) Limited, Lagos Nigeria. Softwareshop Limited & Media Centre has grown to be Fortune 2 companies, a leading provider of INTEGRATED Information Technology Solutions for businesses across several industries. By basing ourselves on the features demanded by larger companies, we have created innovative, user-friendly applications that are now available to small and medium-sized companies.\n\nSoftwareshop Limited deals in a range of software products that support different business processes and functions. We sell genuine software and also beat any verified price. Softwareshop Limited offers installation, configuration & training services for all the software applications we sell/support. We will also offer a FREE consulting advice on which software features match your business requirements.\n\nOur expertise in Hardware and Software, Data, Voice, Power & Security Infrastructure Specialists, with extensive knowledge of Business Applications, IT Support Services and in proven expertise with strong track record of delivery with experience in multiple industries. Provided us with the knowledge to develop solutions that answer the needs of today's clients. These solutions allow you to:\n - increase productivity\n - reduce the operating costs\n - increase customer satisfaction\n\nMoreover, we have recently received the Best B2B Partner from Kaspersky Lab, Microsoft Certified Partner, G data Authorized Partner and many more, please see attached Softwareshop Limited Co-operate Profile for more information. Please take a few minutes to read the enclosed documents. See how Softwareshop Limited's expertise in Hardware and Software can optimize your company's philosophy. I invite you to contact us today so that we can discuss in details how we can help you.\n\nThank you of the interest that you have shown in Softwareshop Limited.\n\nYours sincerely,\nJoy Olasogba\nDigital Marketer\n08037990018, 08080808585\njoy@softwareshopltd.com".format(self.date, self.address)

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

#        try:
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

#        except:
#            print("error sending message")



def main():
    while (0<1):

        print("********************************************\n\n CUSTOMER MESSENGER SOFTWARE.\n\n********************************************\n\nEnter the corresponding number to do any of the following;\n  1.    Add a new customer\n  2.    Print a user message\n  3.    Print all users information(no message)\n  4.    Print all users mssages\n  5.    Send mail to all customers\n  6.    Quit\n\n" )

#        try:
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

#        except:
#            print(">>>>> Wrong value inputed <<<<<\n")


if __name__ == '__main__':
    main()
