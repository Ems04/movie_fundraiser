def yes_no (question):

    error = "Please answer with yes or no."

    valid = False
    while not valid:

        # Ask question and put response is lowercase
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print(error)

# Main routine goes here
for item in range(0, 6):
    want_snack = yes_no("Would like to have some snacks? ")
    print("Answer okay. You said: {}".format(want_snack))
    print()
