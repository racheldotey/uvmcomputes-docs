from itertools import chain
import random

class RandomNumbers:
    numbers = []
    
    def __init__ (self):
        self.minRand = 0
        self.maxRand = 999
        self.count = 10000

    def makeMany (self):
        self.numbers = list()
        self.numbers.append("Start with Min = " + str(self.minRand) + " Max = " + str(self.maxRand) + " Count = " + str(self.count))
        for n in range(self.count):
            self.numbers.append(self.getNum())

        self.numbers.append("Done")
        return(self.numbers)
        
    def getNum (self):
        return(random.randint(self.minRand, self.maxRand))
        
def runRandomNumbers():
    randomNumbers = RandomNumbers()
    return(randomNumbers.makeMany())

runRandomNumbers()