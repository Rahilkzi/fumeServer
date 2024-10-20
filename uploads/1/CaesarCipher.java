Implementation Substitution and Transposition Cipher Text. Design and implement algorithm to encrypt and decrypt message using classical substitution and transposition techniques
import java.util.Scanner;
public class CaesarCipher {
 public static final String ALPHABET = "abcdefghijklmnopqrstuvwxyz";
 public static String encrypt(String plainText, int shiftKey) {
 plainText = plainText.toLowerCase();
String cipherText = "";
for (int i = 0; i < plainText.length(); i++) {
char currentChar = plainText.charAt(i);
 int charPosition = ALPHABET.indexOf(currentChar);
 if (charPosition == -1) {
cipherText += currentChar;
} else {
int keyVal = (shiftKey + charPosition) % 26;
if (keyVal < 0) {
keyVal = ALPHABET.length() + keyVal;
}
char replaceVal = ALPHABET.charAt(keyVal);
cipherText += replaceVal;
}}
return cipherText;
 }
public static String decrypt(String cipherText, int shiftKey) {
cipherText = cipherText.toLowerCase();
String plainText = "";
for (int i = 0; i < cipherText.length(); i++) {
char currentChar = cipherText.charAt(i);
int charPosition = ALPHABET.indexOf(currentChar);
if (charPosition == -1) {
plainText += currentChar;
} else {
int keyVal = (charPosition - shiftKey) % 26;
if (keyVal < 0) {
keyVal = ALPHABET.length() + keyVal;
}
char replaceVal = ALPHABET.charAt(keyVal);
plainText += replaceVal;
}  }
return plainText;
}
 public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
System.out.println("Enter the String for Encryption:");
String message = sc.nextLine(); // Use nextLine() to read the entire line
int shiftKey = 3; // You can change the shift key here
String encryptedMessage = encrypt(message, shiftKey);
System.out.println("Encrypted message: " + encryptedMessage);

String decryptedMessage = decrypt(encryptedMessage, shiftKey);
System.out.println("Decrypted message: " + decryptedMessage);
sc.close();
}}
