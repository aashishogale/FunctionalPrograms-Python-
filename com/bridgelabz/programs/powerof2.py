import sys
from com.bridgelabz.utility.Utility import Utility
class PowerOf2:
    def start(self):
        number=int(sys.argv[1])
        print(number)
        for i in Utility().powerof2(number):
            print(i)
        return

PowerOf2().start()