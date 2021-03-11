import os

print("							V1.0")
print("							Coded by : Gokul \n")

result = ''
message = ''
choice = ''
msg = ''
status = ''
char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
while choice !=0:
    choice = input("Enter the mode : Encode(E) or Decode(D) :  ")

    if choice == 'E':
        message = input("\nEnter the message to Encrypt:  ")
        for c in char:
            if c in message:
                print("The use of LowerCase Letters,Numbers and Symbols are not allowed.")
                status = "False"
                break
        if "False" in status:
            continue
        for c in range(0, len(message)):
            result = result + chr(ord(message[c]) - 11)
        print("\n Your Encrypted Message : ",  result + '\n\n')
        result = ''
        print("\n============= Thank you for using my program============== ;)")
        exit()
    elif choice == 'D':
        message = input("\n Enter the message to Decrypt :  ")
        for c in range(0, len(message)):
            result = result + chr(ord(message[c]) + 11)
        print("\n Your Decrypted Message : ", result + '\n\n')
        result = ''
        print("\n============= Thank you for using my program============== ;)")
        exit()
        break
    elif choice != '0':
        print("You Have Entered an Invalid Input ! \n\n")




