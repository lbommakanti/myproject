from helpers import alphabet_position, rotate_character

def encrypt(text,rot):
    encrypt_text = ""
    for each_char in text:
        #print("Each letter in text: ", each_char)
        rotate_char = rotate_character(each_char,rot)
        # to rotate the char in text
        encrypt_text = encrypt_text + rotate_char
    return encrypt_text

def main():
    msg = input("enter letter: ")
    shift = int(input("Enter no of shift: "))
    #print("alphabet_position ", alphabet_position(msg))
    #print("print rotate_character ", rotate_character(msg,shift))
    print("Encrtped text =  ", encrypt(msg,shift))

if __name__ == "__main__":
    main()
