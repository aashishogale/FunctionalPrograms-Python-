from com.bridgelabz.utility import Utility

class Toss:

    def start(self):
        tossno = int(input('enter the no of tosses'))
        utility=Utility.Utility()
        headsno = utility.calchead(tossno)
        print(headsno)
        return
toss=Toss()
toss.start()

