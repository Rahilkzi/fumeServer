import javax.crypto.*;
import java.io.*;
import java.security.InvalidAlgorithmParameterException;
import java.security.spec.*;
import javax.crypto.spec.IvParameterSpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class DES {
    Cipher ecipher;
    Cipher dcipher;

    DES(SecretKey key) {
        try {
            ecipher = Cipher.getInstance("DES");
            dcipher = Cipher.getInstance("DES");
            ecipher.init(Cipher.ENCRYPT_MODE, key);
            dcipher.init(Cipher.DECRYPT_MODE, key);
        } catch (javax.crypto.NoSuchPaddingException e) {
        } catch (java.security.NoSuchAlgorithmException e) {
        } catch (java.security.InvalidKeyException e) {
        }
    }

    public String encrypt(String str) {
        try {
            byte[] utf8 = str.getBytes(StandardCharsets.UTF_8);
            byte[] enc = ecipher.doFinal(utf8);
            return Base64.getEncoder().encodeToString(enc);
        } catch (javax.crypto.BadPaddingException | IllegalBlockSizeException e) {
            e.printStackTrace();
        }
        return null;
    }

    public String decrypt(String str) {
        try {
            byte[] dec = Base64.getDecoder().decode(str);
            byte[] utf8 = dcipher.doFinal(dec);
            return new String(utf8, StandardCharsets.UTF_8);
        } catch (javax.crypto.BadPaddingException | IllegalBlockSizeException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static void main(String args[]) {
        System.out.println();
        System.out.println("------Encrypting string using DES-----");
        System.out.println();
        try {
            SecretKey key = KeyGenerator.getInstance("DES").generateKey();
            DES encrypter = new DES(key);
            String s = "Chota_Don.!";
            String d = "Hello";
            String encrypted = encrypter.encrypt(s);
            String decrypted = encrypter.decrypt(encrypted);
            System.out.println("Original string is: " + s);
            System.out.println("Encrypted string is: " + encrypted);
            System.out.println("Decrypted string is: " + decrypted);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
