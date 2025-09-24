# Unit Converter Project in Python

def length_converter():
    print("\nLength Converter")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = int(input("Choose conversion (1/2): "))

    if choice == 1:
        km = float(input("Enter value in Kilometers: "))
        miles = km * 0.621371
        print(f"{km} Kilometers = {miles:.2f} Miles")
    elif choice == 2:
        miles = float(input("Enter value in Miles: "))
        km = miles / 0.621371
        print(f"{miles} Miles = {km:.2f} Kilometers")
    else:
        print("Invalid choice!")


def weight_converter():
    print("\nWeight Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = int(input("Choose conversion (1/2): "))

    if choice == 1:
        kg = float(input("Enter value in Kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} Kilograms = {pounds:.2f} Pounds")
    elif choice == 2:
        pounds = float(input("Enter value in Pounds: "))
        kg = pounds / 2.20462
        print(f"{pounds} Pounds = {kg:.2f} Kilograms")
    else:
        print("Invalid choice!")


def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Choose conversion (1/2): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius:.2f}°C")
    else:
        print("Invalid choice!")


def main():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            length_converter()
        elif choice == 2:
            weight_converter()
        elif choice == 3:
            temperature_converter()
        elif choice == 4:
            print("Exiting Unit Converter. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
