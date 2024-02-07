public class UtilityClasses {

    // Konvertiert Dp (Density-independent Pixels) in Pixel
    public static int dpToPx(int dp, Context context) {
        return (int) (dp * context.getResources().getDisplayMetrics().density);
    }

    // Konvertiert Pixel in Dp (Density-independent Pixels)
    public static int pxToDp(int px, Context context) {
        return (int) (px / context.getResources().getDisplayMetrics().density);
    }

    // Formatierung einer Zeitangabe in Millisekunden in ein lesbare String-Format
    public static String formatTime(long millis) {
        int seconds = (int) (millis / 1000) % 60;
        int minutes = (int) ((millis / (1000 * 60)) % 60);
        int hours = (int) ((millis / (1000 * 60 * 60)) % 24);

        return String.format("%02d:%02d:%02d", hours, minutes, seconds);
    }

    // Weitere allgemeine Hilfsfunktionen können hier hinzugefügt werden
}
