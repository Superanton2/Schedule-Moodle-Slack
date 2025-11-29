from login import registration


def main():
    while True:
        print("Hello")
        user = registration()
        if user:
            print(user)




if __name__ == "__main__":
    main()