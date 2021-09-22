#-------------------------------------------------------------------------------
#               Tom Lytle
#           Project 1: Employee Discount
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#   Project 1    Function Area
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
#   Finction name:  EmployeeOrManager
#   Function to validate employee or manager as input
#-------------------------------------------------------------------------------

def EmployeeOrManager():
    Manager = set(['Manager', 'M', 'm', 'manager'])
    Employee = set(['E', 'e', 'Employee', 'employee'])
    global strManager 
    while True:
        choice = input("Are you a Manager or Employee? Enter Manager or Employee:  ")
        if choice in Manager:
                strManager = True
                return True
        elif choice in Employee:
                strManager = False
                return  False
        else:
            print("Please respond with Manager or Employee")



#-------------------------------------------------------------------------------
#   Function Name ValidateYearsOfService
#   Function to validate years of service as an integer
#-------------------------------------------------------------------------------

def ValidateYearsOfService( int_Input ):

    global strFlag

    try:
        int_Input = int(int_Input)
        if (int_Input > 0):
            strFlag = True

        else:
         print("Integer must be positive")

    except ValueError:
        strFlag = False
        print("Must be a number")
    return int_Input 



#-------------------------------------------------------------------------------
#   Function Name: ValidatePrice
#   Function to validate price of item
#-------------------------------------------------------------------------------

def ValidatePrice (dbl_input):
    global strFlag

    try:
        dbl_input = float(dbl_input)
        if (dbl_input > 0 ) and (dbl_input != str):
                strFlag = True

        else:
            print("Must be a positive number")

    except ValueError:
            strFlag = False
            print("Must be a number")
    return dbl_input



#-------------------------------------------------------------------------------
#   Funciton Name: ValidateAddNewEmployee
#   function used to validate input for adding employee yes or no
#-------------------------------------------------------------------------------


def ValidateAddNewEmployee():
    Yes = set(['Yes', 'yes', 'Y', 'y'])
    No = set(['No', 'no', 'n', ])
    global strAddEmployeeFlag
    while True:
        choice = input("Do you want to add another employee? Yes or No: ")
        if choice in Yes:
            strAddEmployeeFlag = True
            return True
        elif choice in No:
            strAddEmployeeFlag = False
            return False
        else:
            print("Must be Yes or No")



#-------------------------------------------------------------------------------
#   Function Name ManagerInputs
#   Gather Managment input for price, years of service, and total purcahse for the year and validate them
#-------------------------------------------------------------------------------    

def ManagerInputs():
    global strFlag
    global intYearsServiceManager
    global dblYearBoughtGoodsManager
    global dblTodaysPurchaseManager

    while strFlag is False:
        intYearsServiceManager = input("Enter years of service: ")
        intYearsServiceManager = ValidateYearsOfService (intYearsServiceManager)

    strFlag = False

    while strFlag is False:
        dblYearBoughtGoodsManager = input("Enter the total price of goods bought this year: ")
        dblYearBoughtGoodsManager = ValidatePrice(dblYearBoughtGoodsManager)

    strFlag = False

    while strFlag is False:
        dblTodaysPurchaseManager = input("Enter price of today's good for purchase: ")
        dblTodaysPurchaseManager = ValidatePrice(dblTodaysPurchaseManager)

    strFlag = False



#-------------------------------------------------------------------------------
#Function Name: EmployeeInputs
# Gather Employee input for price, years of service, and total purcahse for the year and validate them
#-------------------------------------------------------------------------------

def EmployeeInputs():
    global strFlag
    global intYearsServiceEmployee
    global dblYearBoughtGoodsEmployee
    global dblTodaysPurchaseEmployee

    while strFlag is False:
        intYearsServiceEmployee = input("Enter years of service: ")
        intYearsServiceEmployee = ValidateYearsOfService(intYearsServiceEmployee)

    strFlag = False

    while strFlag is False:
        dblYearBoughtGoodsEmployee = input("Enter the total price of good bought this year: ")
        dblYearBoughtGoodsEmployee = ValidatePrice(dblYearBoughtGoodsEmployee)

    strFlag = False

    while strFlag is False:
        dblTodaysPurchaseEmployee = input("Enter price of goods for today's purchase: ")
        dblTodaysPurchaseEmployee = ValidatePrice(dblTodaysPurchaseEmployee)
        
    strFlag = False



#-------------------------------------------------------------------------------
# Function name ManagerDiscount
#   used to calcualte manager discount
#-------------------------------------------------------------------------------

def ManagerDiscount():

    global dblManagerDiscountRate

    if intYearsServiceManager < 4:
        dblManagerDiscountRate = .2
    elif intYearsServiceManager < 7:
        dblManagerDiscountRate = .24
    elif intYearsServiceManager <11:
        dblManagerDiscountRate = .3
    elif intYearsServiceManager < 15:
        dblManagerDiscountRate = .35
    else:
        dblManagerDiscountRate = .4
    print("Discount Rate is:", "{:.0%}".format(dblManagerDiscountRate))

 
    

#-------------------------------------------------------------------------------
#Function Name: EmployeeDiscount
#Function used to calculate employee discount
#-------------------------------------------------------------------------------

def EmployeeDiscountRate():
    
    global dblEmployeeDiscountRate

    if intYearsServiceEmployee < 4:
        dblEmployeeDiscountRate = .1
    elif intYearsServiceEmployee < 7:
        dblEmployeeDiscountRate = .14
    elif intYearsServiceEmployee < 11:
        dblEmployeeDiscountRate = .2
    elif intYearsServiceEmployee < 15:
        dblEmployeeDiscountRate = .25
    else:
        dblEmployeeDiscountRate = .3
    print("Discount Rate is:", "{:.0%}".format(dblEmployeeDiscountRate))
           

#-------------------------------------------------------------------------------
#Function Name YearTotalDiscountManager
#Function used to calculte years total discounts fro managers
#-------------------------------------------------------------------------------

def YearTotalDiscountManager():

    global dblYearTotalDiscountManager

    if strManager is True:
        dblYearTotalDiscountManager = dblYearBoughtGoodsManager * dblManagerDiscountRate
        if dblYearTotalDiscountManager > 200:
            dblYearTotalDiscountManager = 200
        else:
            dblYearTotalDiscountManager = dblYearBoughtGoodsManager * dblManagerDiscountRate
    else:
        dblYearTotalDiscountManager = 0
    print("Total discount for the year:", "${:,.2f}".format(dblYearTotalDiscountManager))




#-------------------------------------------------------------------------------
#Function name: YearTotalDiscountEmployee
#Function used to calculte years total discounts for employees
#-------------------------------------------------------------------------------

def YearTotalDiscountEmployee():
    global dblYearTotalDiscountEmployee
    if strManager is False:
        dblYearTotalDiscountEmployee = dblYearBoughtGoodsEmployee * dblEmployeeDiscountRate
        if dblYearTotalDiscountEmployee > 200:
            dblYearTotalDiscountEmployee = 200
        else:
            dblYearTotalDiscountEmployee = dblYearBoughtGoodsEmployee * dblEmployeeDiscountRate
    else:
        dblYearTotalDiscountEmployee = 0
    print("Total discount for the year is:", "${:,.2f}".format(dblYearTotalDiscountEmployee))




#-------------------------------------------------------------------------------
#Function Name: TodaysDiscountManager
#Function used to calculte todays discount for managers
#-------------------------------------------------------------------------------

def TodaysDiscountManager():

    global dblTodaysDiscountManager

    if dblYearTotalDiscountManager == 200:
        dblTodaysDiscountManager = 0
    elif dblYearTotalDiscountManager < 200:
        dblTodaysDiscountManager = (dblTodaysPurchaseManager * dblManagerDiscountRate)
        if dblTodaysDiscountManager < 0:
            dblTodaysDiscountManager = (200 - dblYearTotalDiscountManager)
        elif (dblTodaysDiscountManager + dblYearTotalDiscountManager) > 200:
            dblTodaysDiscountManager = (200 - dblYearTotalDiscountManager)


    print("Total discount for the today is:", "${:,.2f}".format(dblTodaysDiscountManager))




#-------------------------------------------------------------------------------
#Function Name: TodaysDiscountEmployee
# Function used to calculte todays discount for employees
#-------------------------------------------------------------------------------  

def TodaysDiscountEmployee():

    global dblTodaysDiscountEmployee

    if dblYearTotalDiscountEmployee == 200:
        dblTodaysDiscountEmployee = 0
    elif dblYearTotalDiscountEmployee < 200:
        dblTodaysDiscountEmployee = (dblTodaysPurchaseEmployee * dblEmployeeDiscountRate)
        if dblTodaysDiscountEmployee < 0:
            dblTodaysDiscountEmployee = (200 - dblYearTotalDiscountEmployee)
        elif (dblTodaysDiscountEmployee + dblYearTotalDiscountEmployee) > 200:
            dblTodaysDiscountEmployee = (200 - dblYearTotalDiscountEmployee)


    print("Total discount for the today is:", "${:,.2f}".format(dblTodaysDiscountEmployee))
#-------------------------------------------------------------------------------
#Function Name:     ManagerFunctions
# function used  to call all manager functions
#-------------------------------------------------------------------------------

def ManagerFunctions():

    global dblTodayDiscountManager
    global dblTodaysPurchaseManager
    global dblTodaysPurchaseFinalCost

    ManagerInputs()
    ManagerDiscount()
    YearTotalDiscountManager()
    print("Pre-Discount total is:", "${:,.2f}".format(dblTodaysPurchaseManager))
    TodaysDiscountManager()

    dblTodaysPurchaseFinalCost = (dblTodaysPurchaseManager - dblTodaysDiscountManager)
   
    print("Total due today:", "${:,.2f}".format(dblTodaysPurchaseFinalCost))




#-------------------------------------------------------------------------------
#Function Name: EmployeeFunctions
#Function used to call all Employee functions
#-------------------------------------------------------------------------------

def EmployeeFunctions():

    global dblTodayDiscount
    global dblTodaysPurchaseEmployee
    global dblTodaysPurchaseFinalCost

    EmployeeInputs()
    EmployeeDiscountRate()
    YearTotalDiscountEmployee()
    print("Pre-Discount total is:", "${:,.2f}".format(dblTodaysPurchaseEmployee))
    TodaysDiscountEmployee()

    dblTodaysPurchaseFinalCost = (dblTodaysPurchaseEmployee - dblTodaysDiscountEmployee)

    print("Total due today is:", "${:,.2f}".format(dblTodaysPurchaseFinalCost))



#-------------------------------------------------------------------------------
#Function Name: ExecuteManagerEmployee
#Used to run the ManagerFunction or EmployeeFunction based off of Manager or Employee selection in the
#ManagerOrEmployee Funtion that is written on lines 18-31 
#-------------------------------------------------------------------------------

def ExecuteManagerEmployee():

    global dblTotalPreDiscount
    global dblTotalPostDiscount

    EmployeeOrManager()

    if strManager is True:
        ManagerFunctions()
        dblTotalPreDiscount = (dblTotalPreDiscount + dblTodaysPurchaseManager )
        dblTotalPostDiscount = (dblTotalPostDiscount + dblTodaysPurchaseFinalCost)
    else:
        EmployeeFunctions()
        dblTotalPreDiscount = (dblTotalPreDiscount +  dblTodaysPurchaseEmployee )
        dblTotalPostDiscount = (dblTotalPostDiscount + dblTodaysPurchaseFinalCost)



#-------------------------------------------------------------------------------
#   Project 1 Employee Discount Main Processing Area
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#   Declare Variables
#-------------------------------------------------------------------------------

strManager = False
strFlag = False
strAddEmployeeFlag = True
intYearsServiceManager = int()
dblYearsBoughtGoodsManager = float()
dblTodaysPurchaseManager = float()
intYearsServiceEmployee = int()
dblYearBoughtGoodsEmployee = float()
dblTodaysPurchaseEmployee = float()
dblManagerDiscountRate = float()
dblEmployeeDiscountRate = float()
dblYearTotalDiscountManager = float()
dblYearTotalDiscountEmployee = float()
dblTodaysDiscountManager = float()
dblTodaysDiscountEmployee = float()
dblTodaysPurchaseFinalCost = float()
dblTotalPreDiscount = float()
dblTotalPostDiscount = float()



ExecuteManagerEmployee()


while strAddEmployeeFlag == True:  
    strAddEmployee = ValidateAddNewEmployee()
   
    if strAddEmployee == True:
        
        ExecuteManagerEmployee()

        
    else:
        print("Total Pre-Discount for all staff is:", "${:,.2f}".format(dblTotalPreDiscount))
        print("Total Post-Discount for all staff is:", "${:,.2f}".format(dblTotalPostDiscount))

#Test all manager functions work
#test all employee functions work
#test total for pre and poat discount work
#test having employee and manager inputs calculates correctly
#All displays formatted how I want them