alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",
	"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def alphabet_position(letter):
	#Create our substitution dictionary
	#print("letter: Ahabet[i]", alphabet[i])
	for i in range(0,len(alphabet)):
		if alphabet[i] == letter.lower():
			return i
			# To return the letter which is not in array
	return -1

def rotate_character(char,rot):
	#variable define for char
	alpha_pos = alphabet_position(char)
	#print("alpha_pos : ", alpha_pos)
	# to check the rotate the char to the start 26-1
	if alpha_pos == -1:
		return char
		#to rotate from the start when it reaches to end of array
	new_rot = (alpha_pos + rot) % 26
	#print("alpha_pos-new_rot : ", alpha_pos, "-", new_rot)
	# char is upper char
	if char.isupper():
		return alphabet[new_rot].upper()
	else:
		return alphabet[new_rot]

def encrypt(text,rot):
    encrypt_text = ""
    for each_char in text:
        #print("Each letter in text: ", each_char)
        rotate_char = rotate_character(each_char,rot)
        # to rotate the char in text
        encrypt_text = encrypt_text + rotate_char
    return encrypt_text
