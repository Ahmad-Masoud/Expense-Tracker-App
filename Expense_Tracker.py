import csv
import os

#Saving User Data in a CSV file
def Save_to_CSV(filename, records):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Amount"])
            writer.writerows(records)
        print(f"\nData saved successfully to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

#Validates if the Input for amount is not string
def Digit_Validator(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

#main
def User_input(total_sum):

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
    while True:
        print("Enter\n1: Create New File\n2: Append Previous File\n3: Exit ")
        new_or_append = input("Option: ")

        if new_or_append == "1":
            total_income, total_sum = User_input(total_sum)
            balance = float(total_income) - float(total_sum)
            records.append(["Total Spending: ",total_sum])
            records.append(["Remaining Balance: ",balance])
            print("\nRecords:")
            for r in records:
                print(r)

            print("Total Spending: ",total_sum)
            print("Remaining Balance: ",balance)
            filename = input("Enter File name to Store Data: ")
            Save_to_CSV(filename, records)

            break

        elif new_or_append == "2":
            while True:
                filename = input("Enter File Name to Append or Enter '1' to go back: ")
                if os.path.exists(filename) == True:
                    with open(filename, mode = 'a') as file:
                        records = []
                        user_data(total_sum)
                        writer = csv.writer(file)
                        writer.writerow(records)
                        print("Data Appended Successfully")
                        break
                elif filename == "1":
                    break
                else:
                    print("Invalid Filename")


        elif new_or_append == "3":
            break

        else:
            print("Invalid Option")
