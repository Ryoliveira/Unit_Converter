#! python3
import sys
import time
from Conversion import Converter


def choice():
    while True:
        try:
            conversion_choice = int(input("Enter your choice: "))
            return conversion_choice
        except ValueError:
            print("Enter a valid choice.")


def ask_for_unit():
    while True:
        print("What unit would you like to convert?")
        for i, unit in enumerate(convert.units.keys(), start=1):
            print(i, "|", unit)
        print("Enter 0 at anytime to Exit")
        print("==========================\n")
        user_unit_choice = choice()
        return user_unit_choice


def get_value():
    while True:
        try:
            unit = float(input("Enter value: "))
            return unit
        except ValueError as e:
            print(e)
            print("Enter a valid value above 0.")


def display_options(options):
    print("==================")
    print("Conversion Options")
    print("==================")
    for i, option in enumerate(options, start=1):
        print(i, '|', option)


def cm_conversion():
    display_options(convert.units['cm']['convert_options'])
    conversion_choice = choice()
    choices = len(convert.units['cm']['convert_options']) + 1
    while conversion_choice not in range(choices):
        range_error()
        conversion_choice = choice()
    if conversion_choice == 1:
        print(convert.cm_to_mm(get_value()), "mm")
    if conversion_choice == 2:
        print(convert.cm_to_meter(get_value()), 'meters')
    if conversion_choice == 3:
        print(convert.cm_to_inches(get_value()), 'inches')
    if conversion_choice == 4:
        print(convert.cm_to_feet(get_value()), ' feet')
    if conversion_choice == 0:
        good_bye()


def mm_conversion():
    display_options(convert.units['mm']['convert_options'])
    conversion_choice = choice()
    choices = len(convert.units['mm']['convert_options']) + 1
    while conversion_choice not in range(choices):
        range_error()
        conversion_choice = choice()
    if conversion_choice == 1:
        print(convert.mm_to_cm(get_value()))
    if conversion_choice == 2:
        print(convert.mm_to_inches(get_value()))
    if conversion_choice == 3:
        print(convert.mm_to_feet(get_value()))
    if conversion_choice == 0:
        good_bye()


def meter_conversion():
    display_options(convert.units['meter']['convert_options'])
    conversion_choice = choice()
    choices = len(convert.units['meter']['convert_options']) + 1
    while conversion_choice not in range(choices):
        range_error()
        conversion_choice = choice()
    if conversion_choice == 1:
        print(convert.meter_to_inches(get_value()))
    if conversion_choice == 2:
        print(convert.meter_to_feet(get_value()))
    if conversion_choice == 0:
        good_bye()


def feet_conversion():
    display_options(convert.units['feet']['convert_options'])
    conversion_choice = choice()
    choices = len(convert.units['feet']['convert_options']) + 1
    while conversion_choice not in range(choices):
        conversion_choice = choice()
    if conversion_choice == 1:
        print(convert.feet_to_cm(get_value()))
    if conversion_choice == 2:
        print(convert.feet_to_mm(get_value()))
    if conversion_choice == 3:
        print(convert.feet_to_inches(get_value()))
    if conversion_choice == 4:
        print(convert.feet_to_meter(get_value()))
    if conversion_choice == 0:
        good_bye()


def inches_conversion():
    display_options(convert.units['inches']['convert_options'])
    conversion_choice = choice()
    choices = len(convert.units['inches']['convert_options']) + 1
    while conversion_choice not in range(choices):
        print("Error: Choice out of range.")
        conversion_choice = choice()
    if conversion_choice == 1:
        print(convert.inches_to_cm(get_value()))
    if conversion_choice == 2:
        print(convert.inches_to_mm(get_value()))
    if conversion_choice == 3:
        print(convert.inches_to_meters(get_value()))
    if conversion_choice == 4:
        print(convert.inches_to_feet(get_value()))
    if conversion_choice == 0:
        good_bye()


def miles_conversion():
    display_options(convert.units['miles']['convert_options'])
    conversion_choice = choice()
    choices = len(convert.units['miles']['convert_options']) + 1
    while conversion_choice not in range(choices):
        conversion_choice = choice()
    if conversion_choice == 1:
        print(convert.miles_to_km(get_value()))
    if conversion_choice == 0:
        good_bye()


def km_conversion():
    display_options(convert.units['km']['convert_options'])
    conversion_choice = choice()
    choices = len(convert.units['km']['convert_options']) + 1
    while conversion_choice not in range(choices):
        range_error()
        conversion_choice = choice()
    if conversion_choice == 1:
        print(convert.km_to_miles(get_value()))
    if conversion_choice == 0:
        good_bye()


def good_bye():
    print("Good-bye.")
    sys.exit(0)


def range_error():
    print("Error: Choice out of range.")
    print("Enter a valid option.")


if __name__ == '__main__':
    convert = Converter()
    user_choice = ask_for_unit()
    while user_choice not in range(8):
        range_error()
        time.sleep(1)
        user_choice = ask_for_unit()
    if user_choice == 1:
        cm_conversion()
    if user_choice == 2:
        mm_conversion()
    if user_choice == 3:
        meter_conversion()
    if user_choice == 4:
        feet_conversion()
    if user_choice == 5:
        inches_conversion()
    if user_choice == 6:
        miles_conversion()
    if user_choice == 7:
        km_conversion()
    if user_choice == 0:
        good_bye()
