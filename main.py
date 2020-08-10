import random

class flipCoin:

    def __init__(self):
        self.heads = 0
        self.tails = 0
        self.rounds = int(input("Rounds: "))

    def flip(self):

        for count  in range(0, self.rounds):
            print("Round: " + str(count + 1) + "/" + str(self.rounds))
            coin = random.randint(0,1)
            if coin == 0:
                self.heads += 1
            else:
                self.tails += 1
            count += 1

    def calc(self):

        self.tHeads = self.heads / self.rounds
        self.tTails = self.tails / self.rounds
        print(str(self.tHeads * 100) + "%" + " heads - " + str(self.tTails * 100) + "%" + " tails")

while True:
    run = flipCoin()
    run.flip()
    run.calc()