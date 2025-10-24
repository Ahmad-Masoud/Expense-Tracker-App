
#Validates if the Input for amount is not string
def Digit_Validator(x):
    while True:
        try:
            x = float(x)
            break
        except ValueError:
            x = input("Please Enter Digits: ")

#main
def main(total_sum):

    #User input
    name = input("Enter you name: ")
    income = float(input("Enter Yearly Income: "))
    Digit_Validator(income)
    tax = input("Enter Yearly Tax Amount, If unknown enter 'y' to enter Tax percentage: ")

    if tax == "y" or tax == "Y":
        tax_percentage = float(input("Enter Tax Percentage: "))
        tax = (tax_percentage / 100) * float(income)
        print("Tax = ",tax)
    else:
        Digit_Validator(tax)

    total_sum += tax

    records.append(['Name', name])
    records.append(['Income', income])
    records.append(['Tax', tax])

    user_data(total_sum)
    print(records)

    return income, total_sum

#User Spending Break down and storing the data in array
def user_data(total_sum):

    while True:
        category = input("Enter Category, If Nothing to add enter 'y': ")
        if category == 'y' or category == 'Y':
            break
        else:
            category_amount = float(input("Enter amount spent: "))
            total_sum += category_amount
            records.append([category, category_amount])
    return total_sum


#Public
records = []
total_sum = 0.0

if __name__ == "__main__":
    total_income, total_sum = main(total_sum)
    balance = total_income - total_sum
    print("Total Spending: ",total_sum)
    print("Remaining Balance: ",balance)

