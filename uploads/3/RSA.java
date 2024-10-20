import java.math.*;
import java.security.*;
public class RSA
{
BigInteger p,q,n,d,e,ph,t;
SecureRandom r;
{
r=new SecureRandom();
p=new BigInteger(512,100,r);
q=new BigInteger(512,100,r);
System.out.println("prime nos p and q are"+p.intValue()+","+q.intValue());
n=p.multiply(q);
ph=(p.subtract(new BigInteger("1")));
ph=ph.multiply(q.subtract(new BigInteger("1")));
e=new BigInteger("2");
while(ph.gcd(e).intValue()>1||e.compareTo(ph)!=-1)
e=e.add(new BigInteger("1"));
d=e.modInverse(ph);
System.out.println("public key is("+n.intValue()+","+e.intValue()+")");
System.out.println("pvt key is("+n.intValue()+","+d.intValue()+")");
BigInteger msg=new BigInteger("15");
System.out.println("\nMessage is:"+msg);
BigInteger enmsg=encrypt(msg,e,n);
System.out.println("\nEncryptmsg is:"+enmsg.intValue());
BigInteger demsg=decrypt(enmsg,d,n);
System.out.println("\nDecryptmsg is:"+demsg.intValue());
}
BigInteger encrypt(BigInteger msg,BigInteger e,BigInteger n)
{
return msg.modPow(e,n);
}
BigInteger decrypt(BigInteger msg,BigInteger d,BigInteger n)
{
return msg.modPow(d,n);
}
public static void main(String[]args)
{
new RSA();
}
}
