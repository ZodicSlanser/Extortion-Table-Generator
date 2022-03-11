import pandas
import datetime
from dateutil.relativedelta import relativedelta


def get_full_sheet():

    print("\n\n Your Estimated payment is: " + "{:.3f}".format(payment))
    print("For : " + str(months) + " months")
    print("Starting at " + str(datetime.datetime(byear, bmonth, bday).strftime("%x")))
    print("And ending at " + str(date.strftime("%x")))
    print("A summary of your ammortization table: \n")
    print(df1)


price = float(input("House price: "))
balance = float(price * 0.8)

years = int(input("Years to pay: "))
months = years * 12

yearly_interest_rate = float(float(input("Annual rate: ")) / 100)

interest_rate = float(yearly_interest_rate / 12)


byear = int(input("Starting year : "))
bmonth = int(input("Starting month : "))
bday = int(input("Starting day : "))

ending_balance = 0

df1 = pandas.DataFrame(
    [],
    columns=[
        " Date ",
        " Beginning Balance ",
        " Payment ",
        " Interest ",
        " Principle ",
        " Ending Balance ",
    ],
)
df1.index += 1


payemnt_lhs = float(interest_rate * (1 + interest_rate) ** months)
payment_rhs = float(((1 + interest_rate) ** months) - 1)
payment = float("{:.4f}".format(balance * (payemnt_lhs / payment_rhs)))


date = datetime.datetime(byear, bmonth, bday)
writer = pandas.ExcelWriter("Mortatage.xlsx", engine="xlsxwriter")


for i in range(1, months + 1):
    interest = float("{:.4f}".format(balance * interest_rate))
    principle = float("{:.4f}".format(payment - interest))
    ending_balance = float("{:.4f}".format(balance - principle))

    df1.loc[i] = [
        date.strftime("%x"),
        balance,
        payment,
        interest,
        principle,
        ending_balance,
    ]

    balance = float("{:.5f}".format(ending_balance))
    date += relativedelta(months=1)


while True:
    choice = input(
        "Do you want to print a summary 's' or do you want a full sheet 'f' ? : "
    )

    if choice == "s" or choice == "S" or choice == "f" or choice == "F":

        if choice == "s" or choice == "S":

            get_full_sheet()
            break

        else:

            df1.to_excel(writer, sheet_name="Sheet1", index=1)
            print("Excle Sheet Generated Sucessfully")
            writer.save()
            break

    else:

        print("Sorry only 's' and 'f' can be used")


print("Made With Love by Saif Al-Deen Samir")
