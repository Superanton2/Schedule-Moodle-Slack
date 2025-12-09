"""файл з допоміжними функціями. Тут те що не повʼязане з алгоритмом, але дуже допомагає у взаємодії з програмою"""
RESET = "\033[0m"

RED = "\033[38;5;160m"
YELLOW = "\033[38;5;220m"
BLUE = "\033[0;36;40m"
GREEN = "\33[92m"

def input_to_int(what_you_want_to_ask):
    user_input = input(f"{what_you_want_to_ask}: ")


    while not user_input.isdigit():

        print("Invalid input")
        user_input = input(f"{what_you_want_to_ask}: ")


    user_input = int(user_input)
    return user_input


def lst_input_to_int(choices: list) -> int:
    """check input check as long as not int

    function that checks user input until it enters only a number(int)

    :param choices:
    :return: int of what user input
    """
    question =  make_good_input(choices)
    user_input = input(f"{question}\n» ")


    while not user_input.isdigit():
        print(f"{RED}invalid input{RESET}")
        user_input = input(f"{question}\n» ")


    user_input = int(user_input)

    # якщо вона вибрала неправильно, то вводимо поки не зробить правильно
    while user_input > len(choices) or user_input <= 0:
        print(f"{RED}invalid input{RESET}")
        user_input = input(f"{question}\n» ")

        # тут проблема в тому, що можна ввести не int
        while not user_input.isdigit():
            print(f"{RED}invalid input{RESET}")
            user_input = input(f"{question}\n» ")
        user_input = int(user_input)


    return user_input

def make_good_input(choices: list) -> str:

    result_lst = []
    for index in range(len(choices)):

        result_lst.append(f"{index + 1} - {choices[index]}")

    return "\n".join(result_lst)


def input_to_int(what_you_want_to_ask, max_value= None, min_value= None) -> int:
    user_input = input(f"{what_you_want_to_ask}")


    while not user_input.isdigit():

        print(f"{RED}invalid input{RESET}")
        user_input = input(f"{what_you_want_to_ask}")


    user_input = int(user_input)

    # # зробити перевірку якщо бути лише або макс або мін значення
    # while min_value <= user_input and user_input >= max_value:
    #     print(f"{RED}invalid input{RESET}")
    #     user_input = input(f"{what_you_want_to_ask}")
    #
    #     while not user_input.isdigit():
    #         print(f"{RED}invalid input{RESET}")
    #         user_input = input(f"{what_you_want_to_ask}")
    #
    #     user_input = int(user_input)

    return user_input


