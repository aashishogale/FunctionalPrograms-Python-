from com.bridgelabz.utility import Utility

if __name__ == '__main__':
    newString = input("enter string")
    length = newString.__len__()
    newList=list(newString)
    Utility.Utility().permutations(newString,0)
