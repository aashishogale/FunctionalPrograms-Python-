from com.bridgelabz.utility import Utility
class Windchill:
    def calc(self):

        v=int(input("enter value of v"))
        t=int(input("enter value of t"))
        if(t>50 and (v>120 or v<3)):
            Utility.Utility().windchill(v,t)
        else:
            print("please enter correct value")
            Windchill.calc('self')

        return

windchill1=Windchill
windchill1.calc('self')