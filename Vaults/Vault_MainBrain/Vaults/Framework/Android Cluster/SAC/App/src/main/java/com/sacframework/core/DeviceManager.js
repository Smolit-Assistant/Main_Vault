import java.util.HashMap;
import java.util.Map;

public class DeviceManager {

    private Map<String, DeviceInfo> devices;

    public DeviceManager() {
        devices = new HashMap<>();
    }

    // Fügt ein neues Gerät zum Manager hinzu
    public void addDevice(String deviceId, DeviceInfo info) {
        devices.put(deviceId, info);
    }

    // Entfernt ein Gerät aus dem Manager
    public void removeDevice(String deviceId) {
        devices.remove(deviceId);
    }

    // Überprüft, ob ein Gerät vorhanden ist
    public boolean isDevicePresent(String deviceId) {
        return devices.containsKey(deviceId);
    }

    // Aktualisiert die Informationen eines Geräts
    public void updateDeviceInfo(String deviceId, DeviceInfo newInfo) {
        if (devices.containsKey(deviceId)) {
            devices.put(deviceId, newInfo);
        }
    }

    // Gibt Informationen über ein spezifisches Gerät zurück
    public DeviceInfo getDeviceInfo(String deviceId) {
        return devices.get(deviceId);
    }

    // Weitere Methoden und Logik für die Geräteverwaltung
}

class DeviceInfo {
    private String deviceId;
    private String deviceName;
    private DeviceStatus status;

    public DeviceInfo(String deviceId, String deviceName, DeviceStatus status) {
        this.deviceId = deviceId;
        this.deviceName = deviceName;
        this.status = status;
    }

    // Getter und Setter
}

enum DeviceStatus {
    AVAILABLE,
    BUSY,
    OFFLINE,
    ERROR
}
