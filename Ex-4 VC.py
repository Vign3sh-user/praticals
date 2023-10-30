'''
Write a python program to perform encryption 
and decryption using  the Vigenere cipher 
algorithm.
'''

def generateKey(string,key):
    key=list(key)
    if len(string)==len(key):
        return(key)
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i%len(key)])
    return("".join(key))

def encryption(string,key):
    cipher=[]
    for i in range(len(string)):
        x=(ord(string[i])+ord(key[i]))%26
        x+=ord('A')
        cipher.append(chr(x))
    return("".join(cipher))

def decryption(cipher,key):
    org=[]
    for i in range(len(cipher)):
        x=(ord(cipher[i])-ord(key[i])+26)%26
        x+=ord('A')
        org.append(chr(x))
    return("".join(org))

if __name__ == "__main__":
    string=input("\nEnter the message: ")
    keyword=input("Enter the keyword: ")
    key=generateKey(string,keyword)
    cipher=encryption(string,key)
    print("Encrypted message: ",cipher)
    print("Decrypted message: ",string)
    print()