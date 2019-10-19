#object and classes
class AgeCalculator:

    def calculateAge(self, *dates):

        if ((dates[4]>=dates[1] and dates[3]>=dates[0]) or ((dates[4]>dates[1] and dates[3]<dates[0]))):
            years = (dates[5] - (dates[2]))
            monthdiff = (dates[4] - dates[1])
            monthdiff-=1
            midmonths=monthdiff*30
            remainingdays=(30 - (dates[0]))
            months = ((midmonths+remainingdays+dates[3])//30)
            days = ((midmonths+remainingdays+dates[3])%30)

        else:
            if (dates[4]<=dates[1] and dates[3]<dates[0] or (dates[4]<dates[1] and dates[3]>dates[0])):
                years = (dates[5] - (dates[2]+1))
                monthdiff = (dates[4] + dates[1])
                monthdiff-=1
                midmonths=monthdiff*30
                remainingdays=(30 - (dates[0]))
                months = ((midmonths+remainingdays+dates[3])//30)
                days = ((midmonths+remainingdays+dates[3])%30)

        print('\n-You are {0} years, {1} month(s), and {2} day(s) Old.\n'.format(years, months, days))

    def monthNames(self, *dates1):
        month1 =''
        month0=''
        monthlist = ["","January","February","March","April","May","June","July","August","September","October","November","December"]
        for monthvalues in range(13):#Range starts from 1 and ends at 13-1
            if ((dates1[1]) == (monthvalues)):
                month0 = monthlist[monthvalues]
                break
        for monthvalues in range(13):#Range starts from 1 and ends at 13-1
            if ((dates1[4]) == (monthvalues)):
                month1 = monthlist[monthvalues]
                break
        print('\n\n\n-Your DOB is: {0}th of {1} {2}'.format(dates1[0], month0, dates1[2]))
        print('-Your lookup date is: {0}th of {1} {2}'.format(dates1[3], month1, dates1[5]))


def main():

    confirmInfo = AgeCalculator()
    finalAnswer = AgeCalculator()

    dob = []
    targetYear = []
    tup = ()
    dayob = int(input('\nWelcome, I will tell you exactly how old you are or will be.\nPlease enter your date of Birth below.\n\nDay(1,2,3 ... 31): '))
    dob.append(dayob)
    mob = int(input('Month(01 - 12): '))
    dob.append(mob)
    yob = int(input('Year: '))
    dob.append(yob)
    print('\n\n-Thank You!!\n You need to enter a lookup date(the day you want to know your age).\n')

    tdayob = int(input('-Lookup Day (1-31): '))
    targetYear.append(tdayob)
    tmob = int(input('-Lookup Month (01 - 12): '))
    targetYear.append(tmob)
    tyob = int(input('-Lookup Year: '))
    targetYear.append(tyob)
    tup = (dob[0], dob[1], dob[2], targetYear[0], targetYear[1], targetYear[2])

    confirmInfo.monthNames(*tup)
    finalAnswer.calculateAge(*tup)

if __name__=="__main__":
    main()
