def Digit_Validator(x):
    while True:
        if x.isdigit():
            x = int(x)
            break
        else:
            print("Please Enter Digits: ")
            x = input("Enter Yearly Income: ")

def main():

    #User input
    name = input("Enter you name: ")
    income = input("Enter Yearly Income: ")
    Digit_Validator(income)
    tax = input("Enter Yearly Tax Amount, If unknown enter 'y' to enter Tax percentage: ")
    if tax == "y" or tax == "Y":
        tax_percentage = int(input("Enter Tax Percentage: "))
        tax = (tax_percentage / 100) * int(income)
        print("Tax = ",tax)
    else:
        Digit_Validator(tax)








if __name__ =="__main__":
    main()
