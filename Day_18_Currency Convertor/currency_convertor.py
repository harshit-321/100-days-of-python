print("Currency Converter")

usd_to_inr = 83.0
inr_to_usd = 1 / usd_to_inr

choice = input("1. USD to INR\n2. INR to USD\nEnter your choice: ")

if choice == "1":
    amount = float(input("Enter amount in USD: "))
    print("INR =", amount * usd_to_inr)
elif choice == "2":
    amount = float(input("Enter amount in INR: "))
    print("USD =", amount * inr_to_usd)
else:
    print("Invalid choice!")