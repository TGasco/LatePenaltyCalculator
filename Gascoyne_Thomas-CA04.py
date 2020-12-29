#Student ID: 201419827      Gascoyne_Thomas-CA02.py
#November 2019
#Program which calculates the late penalty for assignments based on raw mark

Loop = True #Global variables

#Defines main function which controls I/O option select
def main(): 
    while Loop == True:
        print("""\t\tMain Menu
\t\t----------------------
\t\t1. Submit an assignment on time
\t\t2. Submit a late assignment
\t\t3. Exit the program
\t\t----------------------""")
        Option = input("\t\tPlease enter an option, either 1, 2, or 3: ")
        while Option not in ("1", "2" , "3"):
            Error_Handle()
            Option = input("\t\tPlease enter an option, either 1, 2, or 3: ")
        if Option == "1":
            #Calls functions associated with option 1
            On_Time()
            Repeat()
        elif Option == "2":
            #Calls functions associated with option 2
            Late()
            Repeat()
        #Terminates program is option 3 is entered
        else:
            exit()

    return

#Defines the function called when option 1 is selected (Assignment on time)    
def On_Time():
    print("""\nThis option is currently under development, apologies for any
inconvenience caused.""")
    return

#Defines the function called when option 2 is selected (Assignment late) 
def Late():
    Count = 0
    Error = True
    while Error == True:
        
        try: #Error handling in case of string input
            Raw_Mark =int(input("Input candidate raw mark for the assignment: "
                                 ))
            if Raw_Mark >= 0 and Raw_Mark <= 100: #Ensures input is in range
                Error = False
            else:
                
                Error_Handle()
        except ValueError:
            Error_Handle()
            
    Error = True
    while Error == True:
        try: #Error handling in case of string input
            Lateness = int(input("Input the number of days late: "))
            if Lateness >= 0 and Lateness <= 7: #Ensures input is in range
                Error = False
            else:
                Error_Handle()
        except ValueError:
            Error_Handle()

    if Error == False:
        print("\n\tDays late\tMarks to award")
        Award_Mark = Raw_Mark
        for i in range(Lateness+1):
            #Loops calculation to show penalties for each day late 
             
            if Award_Mark > 0:
                Penalty = Count*5
                Award_Mark = Raw_Mark - Penalty
            #Ensures candidate is not awarded a negative mark
            else:
                Award_Mark = 0

            #Prints output
            print("\t\t",Count,"\t\t    ",Award_Mark,sep="")
            Count = Count + 1

        #Caps mark if penalty drops it below 40 (Pass threshold)
        if Raw_Mark >= 40 and Award_Mark < 40:
            Award_Mark = 40
            
            print("The mark will be capped at",Award_Mark)
        else:
            pass

        #Calculates whether mark is awarded a pass or fail
        if Award_Mark >= 40:
            Pass = "Pass"
        else:
            Pass = "Fail"

        print("This grade would be awarded a",Pass)
    else:
        pass

    return

#Defines function which asks user if they need the enter another mark (loops)      
def Repeat(Error = True):
    global Loop
    while Error == True:
        Error = True
        Repeat = input("Would you like to enter another grade (Y/N)?: ")
        Repeat = Repeat.upper()
        if Repeat == "Y":
            Error = False
            print("\n")
            
        elif Repeat == "N":
            Error = False
            Loop = False
            exit()
            
        else:
            Error_Handle()
        
    return

#Prints the error message displayed when an invalid input is entered
def Error_Handle():
    print("\nInvalid input - please enter a valid value\n")
    return

#Executes program
main()
