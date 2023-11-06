# Name:  Gabe Dyer 
# Prog Purpose: Finds cost of pet vaccines & medications for dogs and cats
# Not able to tax
# Pricing 
# --------------------
# Canie Vaccines:
# 1.Bordatella $30
# Dapp $35
# Influenza $48
# leptospirosis 21
# Lyme Disease 41
# Rabies 25
# Full 15% dis
# Canine Heartworm Preventative Chews
# Small <25 9.99
# med 26 to 50 11.99
# large 51 to 100 13.99

import datetime

############ define global variables ############
# define Dog prices 
PR_BORD  = 30
PR_DAPP = 35
PR_FLU = 48
PR_ALL = 0
PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

############ define program functions ############
def main():
    more = True
    while more:
        get_user_data()
        if pet_type.upper()== "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()
        askAgain = input("\n would you like process another pet(Y/N)?:  ")
        if askAgain.upper() == "N":
            more = False
            print("Thank you for trusting PET CARE MEDS with your pet vaccines and medications.")
def get_user_data():
    global pet_name, pet_type,pet_weight 
    pet_name= input("pet bame:")
    pet_type = input("Is this pet a dog(D) or cat(C)?")
    pet_weight = input("weight of you pet (in pounds):")
############ dog functions ############
def get_dog_data():
    global pet_vax_type, pet_weight
    dog1 = '\n** Dog Vaccines : \n\t1.bordatella \n\t2.DAPP \n\t3.Influenza \n\t4.Leptospirosis'
    dog2 = '\\n\t5.Influena \n\t6. Lyme Disease \n\t7.Rabies \n\t8.Full Vaccine Pacjage \n\t9.NONE'
    dogmenu = dog1 + dog2
    pet_vax = int((input(dogmenu + '\n** Enter the vaccine number: '))

    print("\nMonthly heart worm prevention medication is recommended for all dog.")
    heart_yesno = input('would you like to order a monthly heartworm medication for ' + pet_name + '(Y/N)?  ")
    if heart_yesno.upper() == 'Y':
                        num_chews = int(input("how many heart work chews would you like to order?"))
def perform_dog_calculations():
    global vax_cost, chews_cost, total
    ###VACS
    if pet_vax_type == 1 :
        vax_cost = PR_BORD
    elif pet_vax_type == 2:
        vax_cost = PR_DAPP
    elif pet_vax_type == 3:
        vax_cost = PR_FLU
    elif 
    else:
        PR_ALL = PR_BORD + PR_DAPP + PR_FLU
        vax_cost = .85 * PR_ALL
    ####### Heart worm chews
    if num_chews != 0:
        if pet_weight < 25:
            chews_cost = num_chews * PR_Chews_SMALL
        elif pet_weight >= 26 and pet_weight < 50:
            chews_cost = num_chews * PR_Chews_MED
        else:
            num_chews * PR_Chews_LARGE

    ####Find total
    total = vax_cost + chews_cost 
    print('DOG CALCS')
def display_dog_results():
     moneyformat = '8,.2f'
    line = '------------------------------------'
    print(line)
    print('**** PET VET ****')
    print(line)
    print('Vaccube amounts      $ ' + format(vax_cost, '8,.2f'))
    print('Chew amount          $ ' + format(chews_cost, '8,.2f'))
    print('Total                $ ' + format(total, '8,.2f'))
    print ('DISPLAY DOGS')

#### CAT functions ####
def get_cat_data():
    print('CAT DATA')
def perform_cat_calculations():
    print("CAT CALCS")
def display_cat_results():
    print('DISPLAY CATS')
    
                        

