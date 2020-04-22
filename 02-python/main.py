SECRET_NUM = 123


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
            elif menu_selection == 0:
                return
            else:
                print("Invalid selection, get real !!")
        except:
            print("An exception occurred")


def choose_app_draw():
    """
        trying to get effect like CLS Clear Screen in console , cursor position top, left

        from os import system, name
        system("cls")

        print("\033[H\033[J")

        cls()
    """

    print("1 - Mood dialog")
    print("2 - Secret number [{}]".format(SECRET_NUM))
    print("3 - Calculator")
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
    while secret_number_input == 0:
        try:
            secret_number_input = int(input("Input secret number [xxx]: "))

            if secret_number_input == SECRET_NUM:
                print("Congratulate !")
            elif secret_number_input == 0:
                print("Are you awake ?")
            elif secret_number_input > SECRET_NUM:
                print("You are too high !")
            elif secret_number_input < SECRET_NUM:
                print("You are too low !")

        except:
            print("An exception occurred")


def calculator():
    """
        - loop dokler ni input prazno polje ali '='?
        - če je string enak dolžini 1 in je eden od '+-*/' je operator, drugače ignore
        - če je string daljši od 0 znakov in je številka +155 ali -5545, če ni število Error

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


choose_app()
