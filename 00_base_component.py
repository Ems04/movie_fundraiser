# Import statements
# Functions go here
# Check that ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

    # If name is not blank, program continues
        if response != "":
            return response
    # If name if blank, show error (& repeat loop)
        else:
            print("This can't be blank, please enter your name.")
# ***** Main Routine *****
# Get up dictionaries / lists needed to hold data
# Ask user if they have used the program before
# Loop to get ticket detail
    # initialise loop so that it runs at least oncea
name = ""
count = 0
MAX_TICKETS = 5

while name != 'xxx' and count < MAX_TICKETS:
    print("You have {} seats left.".format(MAX_TICKETS - count))

    # Get details...

    # Name (can't be blank)
    name = not_blank("Name: ")
    count += 1
    print()

if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. There are {} palce still available.".format(count, MAX_TICKETS - count))

    # Age (between 12 & 130)
    # Calculate ticket price
    # Ask for paymethod (ands apply surcharge if need)
# Calculate total sales and profit
# Output data to text file

