
cust= []
def main():
    read_in_cust_file()
    display_cust_file()
    
def read_in_cust_file():
    cust_data = open("customer_data_file.csv", "r")
    cust_in = cust_data.readlines()
    cust_data.close()

    for i in cust_in:
        cust.append(i.split(","))

def display_cust_file():
    total = 0
    fcurreny = "8,.2f"
    line = "---------------------------------"
    print(line)
    print("******** CUSTOMER SALES REPORT ********\n")
    for i in range(len(cust)):
        amt_owed = float(cust[i][2]) * 1.10
        total  += amt_owed
        print(cust[i][1] + "  \t" + cust[i][0] + '\t' + format(amt_owed,fcurreny))

        print(line)
        print('***** TOTAL AMOUNT:\t$' + format(total, fcurreny))

main()