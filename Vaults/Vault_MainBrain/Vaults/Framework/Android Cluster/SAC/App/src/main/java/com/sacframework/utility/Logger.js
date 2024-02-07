import android.util.Log;

public class Logger {

    private static final String TAG = "SACLogger";

    // Loggt eine Info-Nachricht
    public static void i(String message) {
        Log.i(TAG, message);
    }

    // Loggt eine Warnung
    public static void w(String message) {
        Log.w(TAG, message);
    }

    // Loggt einen Fehler
    public static void e(String message) {
        Log.e(TAG, message);
    }

    // Loggt einen Fehler mit einer Ausnahme
    public static void e(String message, Throwable throwable) {
        Log.e(TAG, message, throwable);
    }

    // Weitere Logging-Funktionen könnten hier hinzugefügt werden
}
