import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class AuthorizationManager {

    private Map<String, Set<String>> userRoles; // Benutzername zu Rollen
    private Map<String, Set<String>> rolePermissions; // Rolle zu Berechtigungen

    public AuthorizationManager() {
        userRoles = new HashMap<>();
        rolePermissions = new HashMap<>();
    }

    // Fügt einem Benutzer eine Rolle hinzu
    public void addUserRole(String username, String role) {
        userRoles.computeIfAbsent(username, k -> new HashSet<>()).add(role);
    }

    // Fügt einer Rolle Berechtigungen hinzu
    public void addRolePermission(String role, String permission) {
        rolePermissions.computeIfAbsent(role, k -> new HashSet<>()).add(permission);
    }

    // Überprüft, ob der Benutzer die angegebene Berechtigung hat
    public boolean checkPermission(String username, String permission) {
        Set<String> roles = userRoles.get(username);
        if (roles == null) {
            return false; // Der Benutzer hat keine Rollen
        }

        for (String role : roles) {
            Set<String> permissions = rolePermissions.get(role);
            if (permissions != null && permissions.contains(permission)) {
                return true; // Berechtigung gefunden
            }
        }

        return false; // Keine Berechtigung gefunden
    }

    // Weitere Autorisierungsmethoden und -logik
}
