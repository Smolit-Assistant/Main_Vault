import android.content.Context;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;

public class NetworkHelper {

    private Context context;

    public NetworkHelper(Context context) {
        this.context = context;
    }

    // Überprüft, ob eine Netzwerkverbindung verfügbar ist
    public boolean isNetworkAvailable() {
        ConnectivityManager connectivityManager = (ConnectivityManager) context.getSystemService(Context.CONNECTIVITY_SERVICE);
        if (connectivityManager != null) {
            NetworkInfo activeNetwork = connectivityManager.getActiveNetworkInfo();
            return activeNetwork != null && activeNetwork.isConnectedOrConnecting();
        }
        return false;
    }

    // Weitere allgemeine Netzwerkfunktionen können hier hinzugefügt werden

    // Beispiel: Methode zur Umwandlung einer IP-Adresse in einen String
    public String ipToString(int ipAddress) {
        return ((ipAddress & 0xff) + "." +
                ((ipAddress >> 8) & 0xff) + "." +
                ((ipAddress >> 16) & 0xff) + "." +
                ((ipAddress >> 24) & 0xff));
    }

    // Beispiel: Methode zur Überprüfung der Verfügbarkeit eines Ports
    public boolean isPortAvailable(int port) {
        // Implementierung zur Überprüfung der Port-Verfügbarkeit
        // Dies könnte beinhalten, den Port zu öffnen und zu sehen, ob eine Ausnahme geworfen wird
        return true; // Vereinfacht angenommen, dass der Port verfügbar ist
    }

    // Weitere Netzwerk-Utility-Funktionen
}
