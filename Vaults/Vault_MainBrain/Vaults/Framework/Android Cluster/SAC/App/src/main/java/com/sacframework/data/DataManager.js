import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DataManager extends SQLiteOpenHelper {

    private static final String DATABASE_NAME = "sacDatabase";
    private static final int DATABASE_VERSION = 1;

    public DataManager(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        // Hier die Datenbanktabellen erstellen
        db.execSQL("CREATE TABLE IF NOT EXISTS data (key TEXT PRIMARY KEY, value TEXT)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // Bei einer Datenbankaktualisierung hier die Änderungen durchführen
    }

    // Speichert einen Wert in der Datenbank
    public void saveData(String key, String value) {
        SQLiteDatabase db = this.getWritableDatabase();
        db.execSQL("INSERT OR REPLACE INTO data (key, value) VALUES (?, ?)", new Object[]{key, value});
        db.close();
    }

    // Liest einen Wert aus der Datenbank
    public String loadData(String key) {
        SQLiteDatabase db = this.getReadableDatabase();
        Cursor cursor = db.rawQuery("SELECT value FROM data WHERE key = ?", new String[]{key});
        if (cursor.moveToFirst()) {
            String value = cursor.getString(0);
            cursor.close();
            db.close();
            return value;
        } else {
            cursor.close();
            db.close();
            return null; // Kein Wert gefunden
        }
    }
}
