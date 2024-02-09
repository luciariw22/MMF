# functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please answer yes/no")


# main routine goes here
while True:
    want_instructions = yes_no("Do you want to read the instructions? ")

    if want_instructions == "yes":
        print("Instructions go here")

    print("program continues...")
    print()
