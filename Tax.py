# Name  Gabe Dyer
# Prog Purpose: Taxes
import datetime
PR_SMALL = 9.99
PR_MEDIUM = 12.99
PR_LARGE = 17.99
PR_EXTRA_LARGE = 21.99
PR_DRINK = 3.99
PR_BREAD = 6.99
RATE_TAX = 0.055

# global variables

numdrink = 0
numbread = 0


######## define program functions ########
def main():
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to tax another vehicle? (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain.upper() == "NO": 
            more = False

def get_user_data():
    
    global carprice, needrelief
    carprice = int(input("\nWhat is the asssesed value of your vehicle: "))
    needrelief = input("Is the vehicle for personal use (Y/N)? ")

def perform_calculations():
    global taxrate, reliefprice,total, value
    value = carprice / 100 * 4.2 /2 
    if needrelief.upper() == "Y":
        reliefprice = value * .33
        total = value - reliefprice 

    else:
        total = value
        reliefprice = 0


def display_results():
    line ='---------------------------------------------'
    moneyf = '>10,.2f'
    print(line)
    print('*********** CITY OF CHARLOTTESVILLE ***********')
    print('***********  PERSONAL PROPERTY TAX ***********')
    print(line)
    print('Assessed Value            $ ' + format(carprice,moneyf))
    print('Full Tax Amount           $ ' + format(value,moneyf))
    print('Relief                    $ ' + format(reliefprice,moneyf))
    print('Total due by DEC 05 2023  $ ' + format(total,moneyf))
    print(line)
    print(str(datetime.datetime.now()))

main()
