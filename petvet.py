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
PR_LEP = 21
PR_LYM = 41
PR_RAB = 25
PR_ALL = 0
PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99
PR_FL = 35
PR_FVR = 30
PR_FRAB = 25
PR_CHEWS_F = 8

############ define program functions ############
def main():
    more = True
    while more:
        get_user_data()

        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()
        askAgain = input("\nWould you like to process another pet(Y/N)?: ")
        if askAgain.upper() == "N" :
            more = False
            print ('Thank you for trusing PET CARE MEDS with your pet bavvines and medications.')
def get_user_data():
    global pet_name, pet_type, pet_weight 
    pet_name = input("Pet name: ")
    pet_type = input("Is this pet a dog(D) or cat (C)? ")
    pet_weight = int(input("Weight of your pet (in pounds): "))
############ dog functions ############
def get_dog_data():
    global pet_vax_type, num_chews, pet_vax
    dog1 = '\n** Dog Vaccines : \n\t1.bordatella \n\t2.DAPP \n\t3.Influenza \n\t4.Leptospirosis'
    dog2 = '\n\t5.Influena \n\t6.Lyme Disease \n\t7.Rabies \n\t8.Full Vaccine Package \n\t9.NONE'
    dogmenu = dog1 + dog2
    pet_vax = int((input(dogmenu + '\n** Enter the vaccine number: ')))

    print("\nMonthly heart worm prevention medication is recommended for all dog.")
    heart_yesno = input("would you like to order a monthly heartworm medication for " + pet_name +   '   (Y/N)?  ' )
    if heart_yesno.upper() == 'Y':
        num_chews = int(input("how many heart work chews would you like to order?: "))
def perform_dog_calculations():
    global vax_cost, chews_cost, total
    ###VACS
    if pet_vax == 1 :
        vax_cost = PR_BORD
    elif pet_vax == 2 :
        vax_cost = PR_DAPP
    elif pet_vax == 3 :
        vax_cost = PR_FLU
    elif pet_vax == 4 :
        vax_cost = PR_LEP
    elif pet_vax == 5 :
        vax_cost = PR_LYM
    elif pet_vax == 6 :
        vax_cost = PR_RAB
    else:
        PR_ALL = PR_BORD + PR_DAPP + PR_FLU + PR_LEP + PR_LYM + PR_RAB
        vax_cost = .85 * PR_ALL
    ####### Heart worm chews
    if num_chews != 0:
        if pet_weight < 25:
            chews_cost = num_chews * PR_CHEWS_SMALL
        elif pet_weight >= 26 and pet_weight < 50:
            chews_cost = num_chews * PR_CHEWS_MED
        else:
            num_chews * PR_CHEWS_LARGE
    else :
        chews_cost = 0
        
    ####Find total
    total = vax_cost + chews_cost 
    print('DOG CALCS')
def display_dog_results():
     moneyformat = '8,.2f'
     line = '------------------------------------'
     print(line)
     print('**** PET VET ****')
     print(line)
     print('vaccines cost        $ ' + format(vax_cost, '8,.2f'))
     print('Chew amount          $ ' + format(chews_cost, '8,.2f'))
     print('Total                $ ' + format(total, '8,.2f'))
     print ('DISPLAY DOGS')

#### CAT functions ####
def get_cat_data():
    global pet_vax_type, num_chews, pet_vax
    catmenu = '\n** Cat Vaccines : \n\t1.Feline Leukemia \n\t2.Feline Biral Rhinotracheitis \n\t3.Rabie (one year)\n\t4.Full Vaccine Package (includes all vaccines)'
    pet_vax = int((input(catmenu + '\n** Enter the vaccine number: ')))
    print("\nMonthly heart worm prevention medication is recommended for all cats.")
    heart_yesno = input("would you like to order a monthly heartworm medication for " + pet_name +   '   (Y/N)?  ' )
    if heart_yesno.upper() == 'Y':
        num_chews = int(input("how many heart work chews would you like to order?: "))
    print('CAT DATA')
def perform_cat_calculations():
    global vax_cost, chews_cost, total
    if pet_vax == 1 :
        vax_cost = PR_FL
    elif pet_vax == 2 :
        vax_cost = PR_FVR
    elif pet_vax == 3 :
        vax_cost = PR_FRAB
    else:
        PR_ALL = PR_FL + PR_FVR + PR_FRAB
        vax_cost = .90 * PR_ALL
    if num_chews != 0:
        chews_cost = num_chews * PR_CHEWS_F
    else:
        chews_cost = 0 
    total = vax_cost * chews_cost 
    print("CAT CALCS")
def display_cat_results():
    moneyformat = '8,.2f'
    line = '------------------------------------'
    print(line)
    print('**** PET VET ****')
    print(line)
    print('vaccines cost        $ ' + format(vax_cost, '8,.2f'))
    print('Chew amount          $ ' + format(chews_cost, '8,.2f'))
    print('Total                $ ' + format(total, '8,.2f'))
     
    print('DISPLAY CATS')
    
                        
main()
