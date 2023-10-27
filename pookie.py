'''
Lab 6: Software Engineering
Encode Function by: Bari Walters
Class: COP3502c
Section Number: 22282
Description: adds 3 to each digit in 8 character password
'''
def encode(password):
    # creates a string to add the increased digits to
    empty_string = ""
    # goes through each digit in the inputed password
    for digit in password:
        # adds 3 to each digit
        empty_string += str(int(digit) + 3)
        # accounts for numbers that will have 2 digits when adding 3 (10, 11, 12)
        if "7" <= digit <= "9":
            # removes 2 digit number from string
            empty_string = empty_string[:-2]
            # adds the two-digit number minus 7 (to make it only the number in the one's place) to the string
            empty_string += str(int(digit) - 7)

    return empty_string


def main():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")
    user_input = int(input("Please enter an option: "))

    while user_input != 3:
        if user_input == 1:
            to_be_encoded = input("Please enter your password to encode: ")
            password = encode(to_be_encoded)
            print("Your password has been encoded and stored?")
        elif user_input == 2:
            to_be_decoded = decode_password(password)
            print(f"The encoded password is {password}, and the original password is {to_be_decoded}")


if __name__ == "__main__":
    main()