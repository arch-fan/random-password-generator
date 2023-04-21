import random

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l', 'm', 'n', 
         'o', 'p', 'q', 'r', 's', 't', 'u', 
         'v', 'w', 'x', 'y', 'z', 'A', 'B', 
         'C', 'D', 'E', 'F', 'G', 'H', 'I', 
         'J', 'K', 'L', 'M', 'N', 'O', 'P', 
         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
         'X', 'Y', 'Z', '0', '1', '2', '3', 
         '4', '5', '6', '7', '8', '9', "@", 
         "#", "$", "%", "&", "=", "<", ">", "-", "."]

def __main__():
    
    pass_length = int(input("Enter password length: "))
    pass_cuantity = int(input("Enter cuantity of passwords: "))

    for i in range(0, pass_cuantity):
    
        password = ''

        for x in range(0, pass_length):
            password += chars[random.randint(0, len(chars) - 1)]

        print(password)

if __name__ == "__main__":
    __main__()