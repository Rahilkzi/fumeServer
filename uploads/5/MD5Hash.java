import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
public class MD5Hash
{
public static void main(String args[])
{
System.out.println("For null"+md5(""));
System.out.println("For simple text"+ md5("My name is SANA"));
System.out.println("For simple numbers"+ md5("321456"));
}
public static String md5(String input)
{
String md5 = null;
if(null==input)
return null;
try{
MessageDigest digest=MessageDigest.getInstance("MD5");
digest.update(input.getBytes(),0,input.length());
md5=new BigInteger(1,digest.digest()).toString(16);
}
catch(NoSuchAlgorithmException e){
e.printStackTrace();
}
return md5;
}
}
