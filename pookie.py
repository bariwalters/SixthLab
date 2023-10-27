"""
Lab 6: Software Engineering
Encode Function by: Bari Walters
Class: COP3502c
Section Number: 22282
Description: adds 3 to each digit in 8 character password
"""


def encode(password):
    # creates a string to add the increased digits to
    empty_string = ""
    # goes through each digit in the given password
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


# Decode Function by: Brian Paz

# The function will shift the numbers down by three
def decode_password(password):
    # The decoded will initialize the empty string to add the shifted numbers
    decoded = ""
    for integer in password:
        # The if statement will account for the numbers shifted down being negative
        if "0" <= integer <= "2":
            # 0 to 7, 1 to 8, 2 to 9
            decoded += str(int(integer) + 7)
        # The else statement will regularly shift the numbers
        else:
            decoded += str(int(integer) - 3)
    return decoded


def main():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit\n""")
    user_input = int(input("Please enter an option: "))
    password = ""
    while user_input != 3:
        # menu option 1
        if user_input == 1:
            to_be_encoded = input("Please enter your password to encode: ")
            # initializes variable to encode
            password = encode(to_be_encoded)
            print("Your password has been encoded and stored!\n")
        # menu option 2
        elif user_input == 2:
            # initializes variable to be decoded
            to_be_decoded = decode_password(password)
            # prints encoded password and original password after its been decoded
            print(f"The encoded password is {password}, and the original password is {to_be_decoded}.\n")
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit\n""")
        user_input = int(input("Please enter an option: "))

if __name__ == "__main__":
    main()
