# Name Gabe Dyer
# Prog Purpose: 
import datetime

############ define global variables ############
# define tax rate and prices
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE= 23.5
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.9

# define global variables
inout = 1 
num_credit  = 0
scholarshipmant = 0

outfile = 'PVCCTICK.html'

############ define program functions ############


def main():
    more = True
    open_outfile()
    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate tuition & fees for another student (Y or N)?: ")
        if yesno == "N" or yesno == "n":
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f 
    f = open(outfile, "w")
    f.write('<html> <head> <title> PVCC TUTION </title>\n')
    f.write('<style> td{text-align: right} </style> <head>\n')
    f.write('<body style ="background-color: #985b45; background-image: url(wp-cinema.png); color: #f8dd61;">\n')


def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = int(input("Scholarship amount received:  "))

#RATE_TUITION_IN = 164.26
#RATE_TUITION_OUT = 336.21
#RATE_CAPITAL_FEE= 23.5
#RATE_INSTITUTION_FEE = 1.75
#RATE_ACTIVITY_FEE = 2.9
def perform_calculations():
    global amount,fee,total,balance, capital,institution,activity
    
    if inout == 1:
        amount  =  RATE_TUITION_IN * numcredits
        fee   = (1.75+2.9)*numcredits
        total = amount+fee
        activity  = 2.9*numcredits
        capital = 0*numcredits
        institution = 1.75*numcredits
        balance = total- scholarshipamt
    
    else:
        amount = RATE_TUITION_OUT*numcredits
        fee = (23.5+1.75+2.9)*numcredits
        total = amount + fee
        capital = 23.5* numcredits
        activity = 2.9*numcredits
        institution = 1.75*numcredits
        balance = total-scholarshipamt
    
    

def display_results():
    moneyformat = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    sp = ' '
    f.write('\n<table border="3"   style ="background-color: #47161a;  font-family: arial; margin: auto;">\n')            
    f.write('<tr><td colspan = 3>\n')
    f.write('<h2>PVCC TUTION</h2></td></tr>')
    f.write('<tr><td colspan = 3>\n')
    f.write('*** Your neighborhood comunity college ***\n')

    f.write(tr + 'Tuition amount' + endtd + str(numcredits) + endtd +   format(amount, moneyformat) + endtr)
    f.write(tr + 'Institutional fee' + endtd + str(numcredits) + endtd + format(institution, moneyformat) + endtr)
    f.write(tr + 'Capital fee ' + endtd + str(numcredits) + endtd + format(capital, moneyformat) + endtr)
    f.write(tr + 'Student activity fee' + endtd + str(numcredits) + endtd + format(activity, moneyformat) + endtr)
    f.write(tr + 'Total amount' + endtd + sp + endtd + format(total, moneyformat) + endtr)
    f.write(tr + 'Scholarship amount' + endtd +sp + endtd + format(scholarshipamt, moneyformat) + endtr)
    f.write(tr + 'Balance' + endtd + sp + endtd + format(balance, moneyformat) + endtr)
    f.write('<tr><td colspan= "3">Date/Time: ')
    f.write(day_time)
    f.write(endtr)
    f.write('</table>')



############ call on main program to execute ############
main()
