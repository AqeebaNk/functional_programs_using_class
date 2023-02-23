from All_Problems_in_1 import All_programs

if __name__ == "__main__":

    # Calling 2D array Program
    # TwoDimentionalArray = All_programs()
    # TwoDimentionalArray.D2_array()

    # #Calling Euclidean Program
    # Euclidean = All_programs()
    # Euclidean.Distance()

    # #Calling Sum Of 3 integer Program
    # sum3 = All_programs()
    # sum3.sum_zero()

    # #Calling QaDratic Program
    # Qadratic1 = All_programs()
    # Qadratic1.Qadratic()

    # #calling Windchill Program
    # windchillprog=All_programs()
    # windchillprog.windchill()


    obj=All_programs()

    while True:


        print("\nEnter the Problem You wanna do\n\n1: Program For 2D Array\n2: Program For Euclidean\n3: Program For Sum Of 3 Integer Is 0\n4: Program For Qadratic Equation\n5: Program For WindChill\n")
        select_option = int(input())

        if   select_option == 1:
            obj.D2_array()

        elif select_option == 2:
            obj.Distance()

        elif select_option == 3:
            obj.sum_zero()

        elif select_option == 4:
            obj.Qadratic()

        elif select_option == 5:
            obj.windchill()

        else:
            print("\nEnter Valid Option\n\n")    
            


