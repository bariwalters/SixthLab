'''
Lab 6: Software Engineering
Encode Function by: Bari Walters
Class: COP3502c
Section Number: 22282
Description: adds 3 to each digit in 8 character password
'''
def encode(password):
    empty_string = ""
    for digit in password:
        empty_string += str(int(digit) + 3)
        if "7" <= digit <= "9":  #make 10, 11, 12
            empty_string = empty_string[:-2]  # "deletes" two digit number
            empty_string += str(int(digit) - 7)  # makes it a single digit number, adds the correct number back

    print(empty_string)


encode("00009962")

# adds 3 to digit 9; adds '12' to string; takes '12' off of string; subtracts 7 from digit 9, adds '2' to string