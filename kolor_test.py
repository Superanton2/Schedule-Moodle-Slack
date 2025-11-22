# кольори для тескту
YELLOW = "\033[38;5;220m"
RESET = "\033[0m"

WHITE = "\033[38;5;255m"

GREEN = "\033[38;5;34m"
RED = "\033[38;5;160m"


with open("test.txt", "a") as file:
    input1 = input("say: ")

    # file.write(f"{YELLOW}{input1}{RESET}\n")
    file.write(f"{input1}")


with open("test.txt", "r") as file:
    for line in file:


        if "## " in line[:4]:

            line.capitalize()
            print(line)
        else:
            print(line)


