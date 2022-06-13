from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def ceasar(direction, message, shift):
    end_text = ""
    
    for letter in message:
        if letter.isalpha():
            if direction == "encode":
                new_position = alphabet.index(letter) + shift
            elif direction == "decode":
                new_position = alphabet.index(letter) - shift
                
            end_text += alphabet[new_position]
        else:
            end_text += letter

    print(f"The {direction} text is {end_text}")

while(True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    
    ceasar(direction, message, shift)

    option = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if(option == "no"):
        print("Goodbye")
        break
