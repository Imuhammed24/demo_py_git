class IntToRoman:

    def method1(self):
        x = 0
        ht = 0
        uu = 0
        low = self.point1-10
        high = self.point1
        for i in range(low, high):

            if (i == self.numb1):
                ht = self.romanK1[self.y1 - 1]
                uu = self.romanV1[x-1]
                print('{0}{1}'.format(ht, uu))#prints final answer
            x+=1

def main():
    instance1 = IntToRoman()
    romanV = ['I','II','III','IV','V','VI','VII','VIII','IX','X']

    romanK = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC','C']

    numb = int(input('Enter a Number: '))

    y = 0
    z = 0
    point = 0
    if (numb % 10) == 0:

        for ten in range(0,110,10):

            if numb == ten:
                print(romanK[z])
            z+=1

    else:
        for numberPoint in range(10,110,10):
            y+=1
            if (numb < numberPoint):
                point = numberPoint

                instance1.numb1 = numb
                instance1.point1 = point
                instance1.y1 = y
                instance1.romanK1 = romanK
                instance1.romanV1 = romanV
                instance1.method1()


if __name__=="__main__":
    main()
