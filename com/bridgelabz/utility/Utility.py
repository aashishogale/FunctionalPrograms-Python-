import random
import math

class Utility:

    def checkhead(self):
        """

        :return:result
        :rtype result:int
        """
        toss = random.random()
        print(toss)
        if (toss < 0.5):
            result = "head"
        else:
            result = "tail"
        print(result)
        return result

    def calchead(self, toss):
        """

        :param toss:
        :type toss: int
        :return:
        :rtype:
        """
        count = 0
        for num in range(0, toss):
            result = Utility.checkhead('self')

            if (result == "head"):
                count += 1

        return count
    def checkLeapYear(self,year):
        """

        :param year:
        :type year:int
        :return:
        :rtype:
        """
        if len(str(year))!=4:

            return ("please enter correct year")
        elif (year%4==0 and year%100!=0)or year%400==0:

            return("it is a leap year")
        else:

            return("it is not a leap year")

    def powerof2(self,max):



        n = 0
        while(n<max):

            yield 2**n
            n +=1



        #
        # if(number>0 and number<32):
        #  for i in range(0,number):
        #     print("2*",i,pow(2,i))
        #     if(i==number):
        #         return
        # else:
        #     return ("pls enter correct number")


    def findharmonic(self,number):
        """

        :param number:
        :type number:int
        :return:
        :rtype:
        """
        result=0
        if (number > 0):
            for i in range(1, number):
               print("1/",i,"+")
               result=result+(1/i)

               if( i == number-1):
                    print("harmonic number",result)
                    return ("")
        else:
            return ("pls enter correct number")

    def findFactors(self,number):
       tempnumber=number



       for i  in range(2,tempnumber):

         while(tempnumber%i==0):
             print(i)
             tempnumber=tempnumber/i


         i=i*i


       return ""


    def gambler(self,stake,goal,nooftimes):
        """

        :param stake:
        :type stake:int
        :param goal:
        :type goal: int
        :param nooftimes:
        :type nooftimes:int
        :return:
        :rtype:
        """
        win=0
        loss=0
        bets=0
        for i in range(0,nooftimes):
            cash=stake
            while(cash>0 and cash<goal):
                toss=random.random()

                if(toss<0.5):
                    cash+=1
                    bets+=1
                else:
                    cash-=1
                    bets+=1
            if(cash==goal):
                win+=1
            if(cash==0):
                loss+=1

        print("no of wins",win,"number of losses",loss,"no of bets",bets)
        return

    def generateRandom(self):

        randomnum=int(1000+(random.random()*(9999-1000)))

        return randomnum

    def countDistinct(self,noofcoupons):
        """

        :param noofcoupons:
        :type noofcoupons: int
        :return:
        :rtype:
        """


        flag=0
        list=[]
        count=1
        list.append(int(self.generateRandom()))
        i=1
        while(i<noofcoupons):

            randomno=self.generateRandom()
            count+=1
            for j in range(0,list.__len__()):
                if(list[j]==randomno):


                    flag=1

            if(flag==0):
                list.append(randomno)
                i=i+1
            else:

                i=i-1


        print("no of random numbers",count)
        print(list)
        return

    def arrayint(self):
        list1=[]
        col=int(input("enter no of columns"))
        rows=int(input("enter no of rows"))

        for i in range(rows):
            list2 =[]
            print("enter rows")
            for j in range(col):
                val=int(input())
                list2.append(val)


            list1.append(list2)




        print(list1)

        return

    def arrayfloat(self):
        """

        :return:
        :rtype:
        """
        list1 = []
        list2= []
        col = float(input("enter no of columns"))
        rows = float(input("enter no of rows"))
        for j in range(0,col):
            print("enter rows")
            for i in range(0, rows):

                list2.append(bool(input()))

            list1.append(list2)



        print(list1)

        return


    def arraybool(self):
        list1 = []
        list2= []
        col = bool(input("enter no of columns"))
        rows = bool(input("enter no of rows"))
        for j in range(0,col):
            print("enter rows")
            for i in range(0, rows):

                list2.append(float(input()))

            list1.append(list2)



        print(list1)

        return

    def triplecount(self):
        array=[]
        count=0
        number=int(input("enter size"))
        for i in range(0,number):
            array.append(int(input()))

        for i in range(0,number):
            for j in range(i+1,number):
                for k in range(j+1,number):
                    if(array[i]+array[j]+array[k]==0):
                        print(array[i],array[j],array[k])
                        count+=1
        print(count)

    def distance(self,pointA,pointB):

        print("distance between",pointA,"and",pointB,math.sqrt(math.pow(pointA,2)+math.pow(pointB,2)))
        return

    def permutations(self, string, step=0):


        if step == len(string):
            print("".join(string))


        for i in range(step, len(string)):

            string_copy = [character for character in string]


            string_copy[step], string_copy[i] = string_copy[i], string_copy[step]


            Utility().permutations(string_copy, step + 1)

        return

    def root(self,a,b,c):
        delta=math.pow(b,2)-4*a*c
        if(delta>=0):
            root1=(-b+math.sqrt(delta))/(2*a)
            root2 = (-b - math.sqrt(delta)) / (2 * a)
            print(root1,"   ",root2)
        else:
            print("please enter crrect root")
        return

    def windchill(self,v,t):
        w=35.74+0.615*t+(0.4275*t-35.75)*math.pow(v,0.16)
        print("windchill",w)
        return
