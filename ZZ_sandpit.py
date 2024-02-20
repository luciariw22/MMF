# A play area for experimenting

# functions go here
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "oui" or response == "ofc":
            return "yes"

        elif response == "no" or response == "nah" or response == "girl no":
            return "no"

        else:
            print("Please answer yes / no")


# main routine goes here
while True:
    want_instructions = yes_no("Do you want to read the instructions? ")

    if want_instructions == "yes":
        print("Instructions go here")

    print("program continues...")
    print()
