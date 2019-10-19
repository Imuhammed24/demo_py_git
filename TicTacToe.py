class TicTacToe:

    def xTurn(self):
        turnX = input("X turn to play: ")
        nav = int(turnX)

        if (turnX == self.arr[nav -1]):

            self.arr[nav-1] = 'X'
            print("\n\n {0} | {1} | {2} \n\n {3} | {4} | {5} \n\n {6} | {7} | {8} \n".format(self.arr[0],self.arr[1],self.arr[2],self.arr[3],self.arr[4],self.arr[5],self.arr[6],self.arr[7],self.arr[8]))
            self.winSequence(self.arr[nav-1])
            self.isFull()

        else:
            print("you cant play in {0}".format(turnX))


    def oTurn(self):
        turnO = input("O turn to play: ")
        navo = int(turnO)

        if (turnO == self.arr[navo-1]):

            self.arr[navo-1] = 'O'
            print("\n\n {0} | {1} | {2} \n\n {3} | {4} | {5} \n\n {6} | {7} | {8} \n".format(self.arr[0],self.arr[1],self.arr[2],self.arr[3],self.arr[4],self.arr[5],self.arr[6],self.arr[7],self.arr[8]))
            self.winSequence(self.arr[navo-1])
            self.isFull()

        else:
            print("you cant play in {0}".format(turnO))


    def winner(self, player):
        print('{0} won'.format(player))
        exit()

    def tie(self):
        print("It's a tie")
        exit()

    def winSequence(self, item):
        if ((item == self.arr[0] and item == self.arr[1] and item == self.arr[2]) or (item == self.arr[3] and item == self.arr[4] and item == self.arr[5]) or (item == self.arr[6] and item == self.arr[7] and item == self.arr[8]) or (item == self.arr[0] and item == self.arr[3] and item == self.arr[6]) or (item == self.arr[1] and item == self.arr[4] and item == self.arr[7]) or (item == self.arr[2] and item == self.arr[5] and item == self.arr[8]) or (item == self.arr[0] and item == self.arr[4] and item == self.arr[8]) or (item == self.arr[2] and item == self.arr[4] and item == self.arr[6])):
            self.winner(item)

    def isFull(self):
        if (('1' in self.arr) or ('2' in self.arr) or ('3' in self.arr) or ('4' in self.arr) or ('5' in self.arr) or ('6' in self.arr) or ('7' in self.arr) or ('8' in self.arr) or ('9' in self.arr)):
            print('')
        else:
            self.tie()


def main():

    object1 = TicTacToe()
    object1.arr = ['1','2','3','4','5','6','7','8','9']

    first = int(input("Who plays first?\n\n 1. X\n 2. O\n\n "))

    if (first == 1):
        print("\n\n {0} | {1} | {2} \n\n {3} | {4} | {5} \n\n {6} | {7} | {8} \n".format(object1.arr[0],object1.arr[1],object1.arr[2],object1.arr[3],object1.arr[4],object1.arr[5],object1.arr[6],object1.arr[7],object1.arr[8]))

        for turns in range(0,5):
            object1.xTurn()
            object1.oTurn()

    elif (first == 2):
        print("\n\n {0} | {1} | {2} \n\n {3} | {4} | {5} \n\n {6} | {7} | {8} \n".format(object1.arr[0],object1.arr[1],object1.arr[2],object1.arr[3],object1.arr[4],object1.arr[5],object1.arr[6],object1.arr[7],object1.arr[8]))

        for turns in range(0,5):
            object1.oTurn()
            object1.xTurn()


if __name__ == '__main__':
    main()
