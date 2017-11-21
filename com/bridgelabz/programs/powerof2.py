import sys
from com.bridgelabz.utility import Utility
class PowerOf2:
    def start(self):
        number=int(sys.argv[1])
        print(number)
        Utility.Utility().powerof2(int(number))
        return

PowerOf2.start('self')