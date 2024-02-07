import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DataManager {

    private static final String TABLE_NAME = "data";
    private static final String COLUMN_KEY = "key";
    private static final String COLUMN_VALUE = "value";
    private DatabaseHelper dbHelper;

    public DataManager(Context context) {
        dbHelper = new DatabaseHelper(context);
    }

    // Fügt neue Daten hinzu oder aktualisiert bestehende
    public void upsertData(String key, String value) {
        SQLiteDatabase db = dbHelper.getWritableDatabase();

        ContentValues values = new ContentValues();
        values.put(COLUMN_KEY, key);
        values.put(COLUMN_VALUE, value);

        db.insertWithOnConflict(TABLE_NAME, null, values, SQLiteDatabase.CONFLICT_REPLACE);
        db.close();
    }

    // Liest Daten basierend auf dem Schlüssel
    public String getData(String key) {
        SQLiteDatabase db = dbHelper.getReadableDatabase();

        Cursor cursor = db.query(TABLE_NAME, new String[]{COLUMN_VALUE}, COLUMN_KEY + " = ?", 
                                 new String[]{key}, null, null, null);
        String value = null;
        if (cursor.moveToFirst()) {
            value = cursor.getString(cursor.getColumnIndex(COLUMN_VALUE));
        }
        cursor.close();
        db.close();
        return value;
    }

    // Hilfsklasse für die Datenbankerstellung und -verwaltung
    private static class DatabaseHelper extends SQLiteOpenHelper {

        private static final String DATABASE_NAME = "SacDatabase";
        private static final int DATABASE_VERSION = 1;

        public DatabaseHelper(Context context) {
            super(context, DATABASE_NAME, null, DATABASE_VERSION);
        }

        @Override
        public void onCreate(SQLiteDatabase db) {
            String createTableSql = "CREATE TABLE " + TABLE_NAME + " (" +
                                    COLUMN_KEY + " TEXT PRIMARY KEY, " +
                                    COLUMN_VALUE + " TEXT)";
            db.execSQL(createTableSql);
        }

        @Override
        public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
            db.execSQL("DROP TABLE IF EXISTS " + TABLE_NAME);
            onCreate(db);
        }
    }
}
