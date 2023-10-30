/*
 Write a Java program to implement the RSA algorithm.
 */

import java.math.*;
import java.util.*;

public class RSAExp {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args)
    {
        //Assigning p, q, n and n2 (Big Integer)
        System.out.print("\nEnter the prime number: ");
        BigInteger p =sc.nextBigInteger();
        System.out.print("Enter another prime number: ");
        BigInteger q =sc.nextBigInteger();
        BigInteger n = p.multiply(q); //p*q
        BigInteger n2 = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE));//(p-1)*(q-1)

        //Assigning encryption(e) and decryption(d) keys
        BigInteger e = generateE(n2);
        BigInteger d = e.modInverse(n2);
        System.out.println("\nEncryption keys: "+e+","+n);
        System.out.println("Decryption keys: "+d+","+n);
        System.out.println();
    }
    private static BigInteger generateE(BigInteger f) {
        Random random = new Random();
        BigInteger e;
        int gcd;
        do {
            e = BigInteger.valueOf(random.nextInt(f.intValue() - 2) + 2);
            gcd = f.gcd(e).intValue();
        } while (gcd != 1);
        return e;
    }
    
}
