import numpy as np
import math
from cmath import sqrt



class All_programs():


    #Program For 2D Array
    def D2_array(self):

        m = int(input("Enter the number of rows: "))
        n = int(input("Enter the number of colomn: "))

        arr = np.arange(1,(m*n)+1).reshape(m,n)
        print(arr)




    #Program For Euclidean 
    def Distance(self):
        x = int(input("Enter the value of x :"))
        y = int(input("Enter the value of y :"))

        formula = (( x *  x)+( y * y))
        print( math.sqrt(formula) )





    #Program for Sum Of 3 integer is 0
    def sum_zero(self):

            arr = []
            n = int(input("Enter how many numbers you want to add : "))

            for i in range(n):
                ele = int(input(f"Enter the {i+1} value of list : "))
                arr.append(ele)


            n = len(arr)
            flag = False
            for i in range(n-2):#1
                for j in range(1,n-1):#0,-1,2
                    for k in range(2,n):#-1,2,-2,,,,,-1,2,-2
                        if((arr[i] + arr[j] + arr[k]) == 0):
                            print(arr[i],arr[j],arr[k])
                            flag = True

            if(flag!=True):
                print("The list does not have  combinations which gives sum of 3 integers equale to Zero")
        



    # Program For Qadratic Equations
    def Qadratic(self):
        a = int(input("Enter the Valve of a: "))
        b = int(input("Enter the Valve of b: "))
        c = int(input("Enter the Valve of c: "))

        delta = (b * b)- (4 * a * c  )

        if a == 0:
            print("Enter valid number")
        else:
            root1 = (-b + sqrt (delta))/ (2 * a)
            root2 = (-b - sqrt (delta))/ (2 * a)

            

            if delta < 0 :
                print("roots are imaginary\n" ,root1,root2)
            elif delta == 0:
                print("roots are real and imaginary\n",root1,root2)
            else:
                print("roots are Distict\n" ,root1,root2)



    #Program For WindChill
    def windchill(self):
        temp = int(input("Enter the temp in Celcius:"))
        speed = int(input("Enter the speed in kilometer :"))

        t = temp + 32
        v = speed * 0.612

        print("\n",t,"Farenheit")
        print(v,"miles\n")

        formula = (13.12 + 0.615 * t - 11.37 * v ** 0.16 + 0.396 * t * v ** 0.16)



        if ( t > 50 or v >= 120):
            print("Enter the valid number")
        else:
            print(formula,"Farenheit")









