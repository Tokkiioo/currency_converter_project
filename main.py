def main():

    print("This program converts US dollars to Euro")
    print()

    dollars = eval(input("Enter amount in dollars: "))

    euros = convert_to_euros(dollars)

    print("That is", euros, "euros.")

convert_to_euros = lambda dollars: dollars * 0.93

main()