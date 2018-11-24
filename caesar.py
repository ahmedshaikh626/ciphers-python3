def de_cipher(ip_text, op_text, cl):
    for i in ip_text:
        if cl == 'e':
            op_text.append( alpha[(alpha.index(i) + key)%26] )
        else:
            op_text.append( alpha[(alpha.index(i) - key)%26] )
    return op_text

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
plaintext = input("Enter the plaintext.  ").upper()
ciphertext = deciphertext = []

while True:
    key = int(input("Enter a key value between 1 and 25 (inclusive).  "))
    if (key == 0 or key == 26):
        print("Cipher text for this key will be same as plaintext. Enter key again.")
    else:
        break

print("Ciphertext:  ", ''.join(de_cipher(plaintext, ciphertext, 'e')))
print("Deciphertext:  ", ''.join(de_cipher(ciphertext, deciphertext, 'd')))