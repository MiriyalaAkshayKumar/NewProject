print("This is cipher program")
from art import logo
print(logo)
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
           ,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def cipher(cipher_text,shift_amount,direction):
    end_text=""
    if direction == 'decode':
        shift_amount *= -1
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift_amount
            end_text += alphabets[new_position]
        else:
            end_text+=char
    print(f"{direction}d text is :{end_text}")

should_continue=True

while should_continue:
    directions = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
    text = input("Enter the message:\n").lower()
    shift = int(input("Enter the number you would like to shift:\n"))
    cipher(text, shift, directions)
    result=input("If you want to continue type 'yes' or to end type 'no'")
    if result == 'no':
        should_continue=False
        print("Good Bye...")
shift = shift % 26
    # def encrypt(plan_text, shift_amount):
    #         cipher_text = ""
    #         for letter in plan_text:
    #             position = alphabets.index(letter)
    #             new_position = position + shift_amount
    #             cipher_text += alphabets[new_position]
    #
    #         print(cipher_text)
    #
    #
    # def decrypt(de_plain_text, de_shif_amount):
    #         de_cipher_text = ""
    #         for letter in de_plain_text:
    #             position = alphabets.index(letter)
    #             new_position = position - de_shif_amount
    #             de_cipher_text += alphabets[new_position]
    #         print(de_cipher_text)
    #
    # if directions=='encode':
    #     encrypt(text, shift)
    #
    # elif directions=='decode':
    #     decrypt(text, shift)
