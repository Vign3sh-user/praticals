/*
 Write a Java program to implement the DES algorithm 
 for encrypting and decrypting a message.
 */


import java.security.*;
import java.io.*;
import javax.crypto.*;
import java.security.spec.*;
class DES
{
    public static void main(String[] args) throws IOException,InvalidKeyException,InvalidKeySpecException,NoSuchAlgorithmException,NoSuchPaddingException,BadPaddingException,IllegalBlockSizeException
    {
        //Message imported
        String msg = "This is a confidential message!";
        byte[] mymsg = msg.getBytes();

        //Key Generation
        KeyGenerator kg=KeyGenerator.getInstance("DES");
        SecretKey DESKey = kg.generateKey();
        
        //Cipher Creation
        Cipher cp=Cipher.getInstance("DES");
        cp.init(Cipher.ENCRYPT_MODE,DESKey);
        byte[] cip=cp.doFinal(mymsg);

        //Decrypter
        cp.init(Cipher.DECRYPT_MODE, DESKey);
        byte[] dt=cp.doFinal(cip);

        //Assigning Values
        String cipherdata = new String(cip);
        String decipher = new String(dt);
        System.out.println("\nMessage: "+msg);
        System.out.println("Encrypted: "+cipherdata);
        System.out.println("Decrypted: "+decipher);
        System.out.println();

    }
}