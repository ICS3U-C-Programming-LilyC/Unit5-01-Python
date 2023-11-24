#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Nov/21/2023
# This program will convert temperatures from celsius to fahrenheit.


def fahrenheit_temp():
    # Explaining my program to the user.
    print(
        "Welcome to my program! It will convert a temperature from celsius (as a decimal) to fahrenheit."
    )

    # Getting the user's temperature.
    user_temp_C_string = input("Enter a temperature in celsius: ")

    # Using a try catch to catch any errors and convert the user's input to a float.
    try:
        user_temp_C_int = float(user_temp_C_string)

        # Calculating the converted temperature.
        temp_F = 9 / 5 * (user_temp_C_int) + 32

        # Displaying the converted temperature to the user.
        print("Your temperature {} °C is {} °F".format(user_temp_C_int, temp_F))

    # Catching any errors.
    except:
        print("Invalid temperature.")


def main():
    # Calling my fahrenheit function.
    fahrenheit_temp()


if __name__ == "__main__":
    main()
