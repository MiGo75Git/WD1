import random as rnd

# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

import msvcrt

secret_num_min = 0
secret_num_max = 25
secret_num = rnd.randrange(secret_num_min, secret_num_max, 1)


# define our clear function
def clear():
    sleep(3)
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def choose_app():
    menu_selection = 0
    while True:
        try:
            choose_app_draw()
            menu_selection = int(input("Selected option please: "))
            if menu_selection == 1:
                mood_dialog()
            elif menu_selection == 2:
                secret_number()
            elif menu_selection == 3:
                calculator()
            elif menu_selection == 4:
                operations_on_strings()
            elif menu_selection == 5:
                miles_to_km_converter()
            elif menu_selection == 6:
                fizz_buzz()
            elif menu_selection == 0:
                return
            else:
                print("Invalid selection, get real !!")
            clear()
        except:
            print("An exception occur red")


def choose_app_draw():
    print("1 - Mood dialog")
    print("2 - Secret number [{0}-{1}]".format(secret_num_min, secret_num_max))
    print("3 - Calculator")
    print("4 - String lowercase,join,formatting, etc...")
    print("5 - Convert km in miles")
    print("6 - FizzBuzz ")
    print("0 - Exit")


def mood_dialog():
    mood = str.lower(input("Enter mood: "))

    if mood == "happy":
        print("It is great to see you happy!")
    elif mood == "nervous":
        print("Take a deep breath 3 times.")
    elif mood == "sad":
        print("Cheer up, mate!")
    elif mood == "exited":
        print("Cool down, mate!")
    elif mood == "relaxed":
        print("Wake up, mate!")
    else:
        print("All OK, mate?")
        print("Hint:[happy],[nervous],[sad],[exited],[relaxed].")


def secret_number():
    secret_number_input = 0
    number_of_retries = 5
    counted_retries = 1
    while not (number_of_retries < counted_retries):
        try:
            secret_number_input = int(input(
                "Input secret number range[{0}-{1}]. Attemp[{2}]".format(secret_num_min, secret_num_max,
                                                                         counted_retries)))
            counted_retries = counted_retries + 1

            if secret_number_input == secret_num:
                print("Congratulate !")
            elif secret_number_input == 0:
                print("Are you awake ?")
            elif secret_number_input > secret_num:
                print("You are too high !")
            elif secret_number_input < secret_num:
                print("You are too low !")
        except:
            print("An exception occurred")


def calculator():
    """
        - IN FUTURE: dva arraya numbers[],operators[] + procesiranje ??
        - na koncu izpis računa in rezultata

        TODO: Fix this bug for * and /
        KNOWN BUGS: At the end displaying equation is wrong
        now: 2+4+2*10=80
        ok : (2+4+2)*10=80
        HOW: at operation * or / put string in brackets, but be aware of last position (multiple brackets)
    """
    end_loop = False
    result = None
    first_number = None
    input_number = 0
    input_operation = equation = ""
    reset_input_after_operation = is_current_input_number = True

    while not end_loop:
        try:
            is_last_operation_error = False
            if is_current_input_number:
                input_string = input("Input number [+-0..9]: ")
            else:
                input_string = input("Input operation [+-*/=]: ")

            if len(input_string) > 0:
                if len(input_string) == 1 and ("+-*/=".__contains__(input_string)):
                    if input_string == "+":
                        input_operation = "+"

                    elif input_string == "-":
                        input_operation = "-"

                    elif input_string == "*":
                        input_operation = "*"

                    elif input_string == "/":
                        input_operation = "/"

                    elif input_string == "=":
                        input_operation = "="
                        print("Result: {0}{1}{2}".format(equation, "=", result))
                        end_loop = True

                    is_current_input_number = True

                else:
                    # must be a number
                    try:

                        input_number = float(input_string)

                        if first_number is None:
                            first_number = input_number
                            if reset_input_after_operation:
                                input_number == 0
                            is_current_input_number = False
                            equation = "{0}".format(first_number)
                        else:

                            if input_operation == "-":
                                result = first_number - input_number

                            elif input_operation == "+":
                                result = first_number + input_number

                            elif input_operation == "*":
                                result = first_number * input_number

                            elif input_operation == "/":
                                try:
                                    result = first_number / input_number
                                except:
                                    is_last_operation_error = True

                            if not is_last_operation_error:
                                if reset_input_after_operation:
                                    input_number == 0
                                is_current_input_number = False
                                equation = "{0}{1}{2}".format(equation, input_operation, input_number)
                                first_number = result

                    except:
                        print("Not valid number")
                        is_last_operation_error = True

                    print(equation)

            elif len(input_string) == 0:
                print("Result: {0}{1}{2}".format(equation, "=", result))
                end_loop = True

        except:
            print("An exception occurred in main loop of calculator")


def operations_on_strings():
    test = "Testna variabla"

    print("Lesson9")
    print(f"Kaj {test}")

    str_one = "Happy"
    str_two = "Day"

    # We can join them with a plus:
    print(str_one + str_two)  # result: HappyDay

    # We can add a string in-between:
    print(str_one + " " + str_two)  # result: Happy Day

    # We can use % s to add them in a string:
    print("%s %s" % (str_one, str_two))

    # We can use %s to add them in a string:
    print("%s %s" % (str_one, str_two))

    # Or, we can use the format() method, with placeholders like {0}:
    print("{0} {1}".format(str_one, str_two))

    # The format function can also be used a bit differently:
    print("{first} {second_str}".format(first=str_one, second_str=str_two))

    # The newest way of formatting strings is called f-string and it looks like this:
    print(f"{str_one} {str_two}")

    # lower case
    print(f"{str_one} {str_two}".lower())

    # upper case
    print(f"{str_one} {str_two}".lower())

    # center string with padding
    print(f"{str_one} {str_two}".center(100, "-"))

    # SWAP CaSe
    print(f"{str_one} {str_two}".swapcase())


def miles_to_km_converter():
    ONE_MILE_KM_FACTOR: float = 0.62137
    stop_loop = False

    print("Welcome !")
    print("This is km to miles converter. Input km and you will get lenght in miles.")

    while not stop_loop:

        try:
            input_string = input("Input kilometers please: ")
            kilometers = float(input_string.replace(",", "."))
            miles = kilometers * ONE_MILE_KM_FACTOR
            print(f"{kilometers} km is equal to {miles} miles.")
        except:
            print("Please insert valid float number")

        sleep(1)

        while True:
            answer_to_continue = input("Do you want convert again ? [y/n]")
            if answer_to_continue.lower() == "n":
                stop_loop = True
                break

            elif answer_to_continue.lower() == "y":
                stop_loop = False
                break

            else:
                print("Please select [y] or [n] !!")

    print("Goodbye ...")


def fizz_buzz():
    count_by_div_3 = 0
    count_by_div_5 = 0
    count_by_div_3_5 = 0

    while True:
        try:
            input_number = int(input("Input number between [1-100]: "))
            if input_number < 1:
                print("Number is too low.")
            elif input_number > 100:
                print("Number is to high.")
            else:
                break
        except:
            print("Enter valid number")

    for i in range(input_number):
        left_by_div_3 = i % 3
        left_by_div_5 = i % 5
        if i >= 3:
            if left_by_div_3 == 0 and left_by_div_5 == 0:
                print(f"{i} Fizz/Fuzz [/5 and /3 = OK]")
                count_by_div_3_5 = count_by_div_3_5 + 1

            elif left_by_div_5 == 0:
                print(f"{i} Fuzz [/5 = OK]")
                count_by_div_5 = count_by_div_5 + 1

            elif left_by_div_3 == 0:
                print(f"{i} Fizz [/3 = OK]")
                count_by_div_3 = count_by_div_3 + 1
            else:
                print(f"{i}")
        else:
            print(f"{i} - too low")

    print(f"Info: {count_by_div_3}-[/3 = OK] {count_by_div_5}-[/5 = OK] {count_by_div_3_5}-[/5 and /3 = OK]")
    print("Successfully ended.")
    sleep(5)

choose_app()
