import android.content.Context;
import android.content.SharedPreferences;

public class ConfigManager {

    private static final String PREFERENCES_FILE_KEY = "com.example.sac.config";
    private SharedPreferences sharedPref;

    public ConfigManager(Context context) {
        sharedPref = context.getSharedPreferences(PREFERENCES_FILE_KEY, Context.MODE_PRIVATE);
    }

    // Speichert eine Konfigurationseinstellung
    public void setConfig(String key, String value) {
        SharedPreferences.Editor editor = sharedPref.edit();
        editor.putString(key, value);
        editor.apply();
    }

    // Liest eine Konfigurationseinstellung
    public String getConfig(String key, String defaultValue) {
        return sharedPref.getString(key, defaultValue);
    }

    // Weitere Methoden für verschiedene Datentypen oder komplexe Konfigurationen
}
