import java.util.HashMap;
import java.util.Map;

public class AuthenticationManager {

    private Map<String, String> userCredentials; // Benutzername und Passwort

    public AuthenticationManager() {
        userCredentials = new HashMap<>();
        // Hier könnten Benutzerdaten aus einer sicheren Quelle geladen werden
    }

    // Fügt einen neuen Benutzer hinzu
    public void addUser(String username, String password) {
        userCredentials.put(username, password);
    }

    // Überprüft die Anmeldeinformationen eines Benutzers
    public boolean authenticateUser(String username, String password) {
        String storedPassword = userCredentials.get(username);
        if (storedPassword == null) {
            return false; // Benutzername existiert nicht
        }
        return storedPassword.equals(password); // Überprüft das Passwort
    }

    // Methode zum Ändern des Passworts eines Benutzers
    public boolean changePassword(String username, String oldPassword, String newPassword) {
        if (authenticateUser(username, oldPassword)) {
            userCredentials.put(username, newPassword);
            return true; // Passwort erfolgreich geändert
        }
        return false; // Altes Passwort ist falsch
    }

    // Weitere Authentifizierungsmethoden und -logik
}
