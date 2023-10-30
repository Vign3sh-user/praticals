'''
Write a python program to perform encryption 
and decryption using the Substitution cipher 
algorithm.
'''

def encrypt(x,y,z):
    keyIndices = [x.index(k) for k in y]
    return ''.join(z[keyIndex] for keyIndex in keyIndices)
    
def decrypt(x,y,z):
    keyIndices = [x.index(k) for k in y]
    return ''.join(z[keyIndex] for keyIndex in keyIndices)

if __name__=="__main__":
    atoz='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,!'
    key='mnopqrstuvwxyz.,!ABCDEFGHIJabcdefghijklKLMNOPQRSTUVWXYZ'
    pt=str(input("\nEnter the plaintext: "))    
    cp=encrypt(atoz,pt,key)
    dp=decrypt(key,cp,atoz)
    print()
    print("Plaintext: ",pt)
    print("Encrypted: ",cp)
    print("Decrypted: ",dp)
    print()
