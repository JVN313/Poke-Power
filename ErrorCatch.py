
def ErrorCatch(name):
    while name is None:
        try:
            name = input("Invalid Input: Please Re-enter Pokemon Name \nEnter Pokemon Name: ")
            return name

        except AttributeError:
            name = input("Invalid Input: Please Re-enter Pokemon Name \nEnter Pokemon Name: ")
            continue

