# Author: Nithin/0x5a
# Version: 1.0 Release 2018
# Status: No Longer Maintained!


result = ''
message = ''
choice = ''

print("##################################0x5a####################################")
print("--------------------------------EDRYPTER----------------------------------")
print("################################v1-2018##################################")
while choice != 0:
    choice = input("\nWelcome to EDRYPTER \n 1. Encrypt \n 2. Decrypt \n 3. Exit \nEnter your Choice: ")

    if choice == '1':
        message = input("\nEnter message for encryption: ")
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - 6) 

        print("\nEncrypted text is: " + result + '\n')
        print("Thank you for using EDRYPTER")
        result = ''

    elif choice == '2':
        message = input("\nEnter the message for decryption: ")
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + 6) 

        print("\nDecrypted text is: " + result + '\n')
        print("Thank you for using EDRYPTER")
        result = ''
        
    elif choice == '3':
        exit()

    elif choice != '0':
        print("Wait What?")
