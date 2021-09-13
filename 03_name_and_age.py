# function goes here

def int_check(question,low,high):

    error = "Please enter a whole number between 12 and 130"

    valid = False
    while not valid:

        # ask user for number and check it's valid
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        # if an integer is not entered, display an error message
        except ValueError:
            print(error)

# main routine goes here
age = int_check("Age: ", 12, 130)

