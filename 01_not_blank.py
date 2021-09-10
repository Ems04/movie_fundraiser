# Function is here
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        while response != "":
            return response
        else:
            print("This can't be blank, please enter your name.")

# Main routine is here
name = not_blank("Name: ")
