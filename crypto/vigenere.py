from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    new_text_with_key = ""
    i = 0
    for orig_char in text:
        #print ("the char: ", char)
        # to check is the char is the text
        if orig_char.isalpha():
            new_char = key[i]
            if i < len(key)-1:
                i = i+1
            else:
                i = 0
        else:
            new_char = orig_char
            # variable create to see the pos of the new_char
        alpa_pos = alphabet_position(new_char)
        # to check the position for original and newchar position
        new_char = rotate_character(orig_char,alpa_pos)
        #print("orig_char - new_char", orig_char, "-", new_char)
        #To check the new_char is the key
        new_text_with_key = new_text_with_key + new_char
        #print ("the new_text_with_key: ", new_text_with_key)
        #print("Each letter in text: ", each_char)
        #rotate_char = rotate_character(each_char,rot)
        #encrypt_text = encrypt_text + rotate_char
    return new_text_with_key


def main():
    #msg = input("enter text: ")
    #key = input("enter the key: ")
    #shift =int(input("Enter no of shift: "))
    #print("alphabet_position ", alphabet_position(msg))
    #print("rotate_character ", rotate_character(msg,shift))
    #print ("Original text = " , msg)
    print("Encrtped text =  ", encrypt("Sailing <3 ships thru br0ken harbors","NeilYoung"))

if __name__ == "__main__":
    main()
