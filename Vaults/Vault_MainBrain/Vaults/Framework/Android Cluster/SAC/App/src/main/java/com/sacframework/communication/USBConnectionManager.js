import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.hardware.usb.UsbManager;
import android.hardware.usb.UsbAccessory;
import android.hardware.usb.UsbDevice;
import android.hardware.usb.UsbDeviceConnection;
import android.hardware.usb.UsbInterface;
import android.hardware.usb.UsbEndpoint;

import java.util.HashMap;

public class USBConnectionManager {

    private UsbManager usbManager;
    private PendingIntent permissionIntent;
    private static final String ACTION_USB_PERMISSION = "com.example.USB_PERMISSION";

    public USBConnectionManager(Context context) {
        usbManager = (UsbManager) context.getSystemService(Context.USB_SERVICE);
        permissionIntent = PendingIntent.getBroadcast(context, 0, new Intent(ACTION_USB_PERMISSION), 0);
    }

    // Entdeckt verfügbare USB-Geräte
    public void discoverDevices() {
        HashMap<String, UsbDevice> deviceList = usbManager.getDeviceList();
        for (UsbDevice device : deviceList.values()) {
            // Fordert die Berechtigung an, um mit dem Gerät zu kommunizieren
            usbManager.requestPermission(device, permissionIntent);
        }
    }

    // Verbindet sich mit einem USB-Gerät
    public void connectToDevice(UsbDevice device) {
        if (!usbManager.hasPermission(device)) {
            // Keine Berechtigung für das Gerät
            return;
        }

        UsbDeviceConnection connection = usbManager.openDevice(device);
        if (connection == null) {
            // Fehler beim Öffnen des Geräts
            return;
        }

        // Wählen Sie eine Schnittstelle und stellen Sie eine Verbindung her
        UsbInterface usbInterface = device.getInterface(0);
        connection.claimInterface(usbInterface, true);

        // Kommunikationslogik hier (z.B. Lesen und Schreiben von Daten)
    }

    // Schließt die Verbindung zu einem USB-Gerät
    public void disconnectDevice(UsbDevice device, UsbDeviceConnection connection) {
        UsbInterface usbInterface = device.getInterface(0);
        connection.releaseInterface(usbInterface);
        connection.close();
    }
}
