import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.KeyGenerator;
import java.security.SecureRandom;
import java.util.Base64;

public class EncryptionManager {

    private static final String ALGORITHM = "AES";
    private static final String TRANSFORMATION = "AES/CBC/PKCS5Padding";

    // Generiert einen zufälligen Schlüssel für die Verschlüsselung
    public SecretKeySpec generateKey() throws Exception {
        KeyGenerator keyGenerator = KeyGenerator.getInstance(ALGORITHM);
        keyGenerator.init(256); // AES-256
        byte[] key = keyGenerator.generateKey().getEncoded();
        return new SecretKeySpec(key, ALGORITHM);
    }

    // Verschlüsselt den gegebenen Text mit dem angegebenen Schlüssel
    public String encrypt(String input, SecretKeySpec key) throws Exception {
        Cipher cipher = Cipher.getInstance(TRANSFORMATION);
        cipher.init(Cipher.ENCRYPT_MODE, key, new IvParameterSpec(new byte[16]));
        byte[] encrypted = cipher.doFinal(input.getBytes());
        return Base64.getEncoder().encodeToString(encrypted);
    }

    // Entschlüsselt den gegebenen Text mit dem angegebenen Schlüssel
    public String decrypt(String input, SecretKeySpec key) throws Exception {
        Cipher cipher = Cipher.getInstance(TRANSFORMATION);
        cipher.init(Cipher.DECRYPT_MODE, key, new IvParameterSpec(new byte[16]));
        byte[] original = cipher.doFinal(Base64.getDecoder().decode(input));
        return new String(original);
    }
}
