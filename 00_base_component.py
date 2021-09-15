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

# integer check
def int_check(question):

    error = "Please enter a whole number between 12 and 130"

    valid = False
    while not valid:
    # ask user for number and check it's valid
        try:
            response = int(input(question))

            if response <=0:
                print(error)
            else:
                return response
    # if an integer is not entered, display an error message
        except ValueError:
            print(error)
# ***** Main Routine *****
# Get up dictionaries / lists needed to hold data
# Ask user if they have used the program before
# Loop to get ticket detail
    # initialise loop so that it runs at least once
MAX_TICKETS = 5
profit = 0
ticket_profit = 0
name = ""
ticket_count = 0
ticket_sales = 0

while name != 'xxx' and ticket_count < MAX_TICKETS:
    if ticket_count < MAX_TICKETS:
        print("You have {} seats left.".format(MAX_TICKETS - ticket_count))
    else:
        print("You have one place left")

    # Get details...
    # Name (can't be blank)
    name = not_blank("Name: ")
    if name == "xxx":
        break
    # Age (between 12 & 130)
    age = int_check("Age: ")

    # check that age is valid
    if age < 12:
        print("Sorry you are too young to watch this movie.")
        continue
    elif age > 130:
        print("This is very old. It looks like you have made a mistake.")
        continue

    # ticket price details
    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    ticket_count += 1
    ticket_sales += ticket_price

# End of ticket loop
# Calculalty profit
ticket_price = ticket_count - (5 * ticket_count)
print("Profit from tickets sales are ${:.2f}".format(ticket_sales))

# Tell user if they have unsold tickets
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. There are {} place still available.".format(ticket_count, MAX_TICKETS - ticket_count))

# Calculate ticket price
profit_made = ticket_price - 5
profit += profit_made

# Ask for paymethod (ands apply surcharge if need)
# Calculate total sales and profit
# Output data to text file

