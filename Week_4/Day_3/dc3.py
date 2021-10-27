choice = ""
shift = 0
encryption_text = ""
decryption_text = ""
alphabet = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
abc = {}  

while choice != "encrypt" or "decrypt":
    choice = input("do you want to encrypt or decrypt: ")
    shift = int(input("by how many do you want to shift: "))
        

    if choice == "encrypt":

        alphabet2 = {key+shift: value for (key, value) in alphabet.items()}
        alphabet_update = {key-26: value for (key, value) in alphabet2.items() if key > 26}

        encryption_text = input("write a sentence you want to encrypt: ").lower
        for letter in encryption_text:
            decryption_text += chr(ord(letter) + shift)
        print(decryption_text)
        break

    elif choice == "decrypt":
        
        alphabet2 = {key+shift: value for (key, value) in alphabet.items()}
        alphabet_update = {key+26: value for (key, value) in alphabet2.items() if key < 26}

        alphabet2.update(alphabet_update)
        decryption_text = input("write a sentence you want to decrypt: ")
        for letter in decryption_text:
            encryption_text += chr(ord(letter) - shift)
        print(encryption_text)
        break


