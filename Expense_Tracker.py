
#Validates if the Input for amount is not string
def Digit_Validator(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

#main
def main(total_sum):

    #User input
    name = input("Enter you name: ")
    income = Digit_Validator("Enter Yearly Income: ")
    tax = input("Enter Yearly Tax Amount, If unknown enter 'y' to enter Tax percentage: ")

    if tax.lower() == "y":
        tax_percentage = Digit_Validator("Enter Tax Percentage: ")
        tax = (float(tax_percentage) / 100) * float(income)
        print("Tax = ",tax)
    else:
        while True:
            try:
                tax = float(tax)
                break
            except ValueError:
                tax = input("Enter Valid Tax Amount: ")

    total_sum += tax

    records.append(['Name', name])
    records.append(['Income', income])
    records.append(['Tax', tax])

    total_sum = user_data(total_sum)

    return income, total_sum

#User Spending Break down and storing the data in array
def user_data(total_sum):

    while True:
        category = input("Enter Category, If Nothing to add enter '1' to Exit: ")
        if category == "1":
            break
        else:
            category_amount = Digit_Validator("Enter amount spent: ")
            total_sum += category_amount
            records.append([category, category_amount])
    return total_sum


#Public
records = []
total_sum = 0.0

if __name__ == "__main__":
    total_income, total_sum = main(total_sum)
    balance = float(total_income) - float(total_sum)

    print("\nRecords:")
    for r in records:
        print(r)

    print("Total Spending: ",total_sum)
    print("Remaining Balance: ",balance)

