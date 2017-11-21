from com.bridgelabz.utility import Utility

if __name__ == '__main__':
    stake = int(input("enter the stake"))
    goal = int(input("enter goal"))
    nooftimes = int(input("no of times"))
    Utility.Utility().gambler(stake, goal, nooftimes)
