def input_to_int(what_you_want_to_ask):
    user_input = input(f"{what_you_want_to_ask}: ")


    while not user_input.isdigit():

        print("Invalid input")
        user_input = input(f"{what_you_want_to_ask}: ")


    user_input = int(user_input)
    return user_input

