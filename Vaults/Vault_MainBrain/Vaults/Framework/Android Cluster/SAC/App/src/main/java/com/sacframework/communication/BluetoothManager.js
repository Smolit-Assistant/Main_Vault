import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothServerSocket;
import android.bluetooth.BluetoothSocket;
import java.io.IOException;
import java.util.Set;
import java.util.UUID;

public class BluetoothManager {

    private final BluetoothAdapter bluetoothAdapter;
    private final UUID myUUID;
    private AcceptThread acceptThread;

    public BluetoothManager() {
        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        myUUID = UUID.fromString("ein-eindeutiger-uuid-string"); // Ersetzen Sie dies durch einen eindeutigen UUID-String
    }

    // Startet den Geräte-Entdeckungsprozess
    public void discoverDevices() {
        if (bluetoothAdapter.isDiscovering()) {
            bluetoothAdapter.cancelDiscovery();
        }
        bluetoothAdapter.startDiscovery();
    }

    // Gibt ein Set von gekoppelten Geräten zurück
    public Set<BluetoothDevice> getPairedDevices() {
        return bluetoothAdapter.getBondedDevices();
    }

    // Startet den Server-Thread, um auf eingehende Verbindungen zu warten
    public void startServer() {
        acceptThread = new AcceptThread();
        acceptThread.start();
    }

    // Verbindet sich mit einem Bluetooth-Gerät
    public void connectToDevice(BluetoothDevice device) {
        ConnectThread connectThread = new ConnectThread(device);
        connectThread.start();
    }

    // Server-Thread, der auf eingehende Verbindungen wartet
    private class AcceptThread extends Thread {
        private final BluetoothServerSocket serverSocket;

        public AcceptThread() {
            BluetoothServerSocket tmp = null;
            try {
                tmp = bluetoothAdapter.listenUsingRfcommWithServiceRecord("SAC", myUUID);
            } catch (IOException e) {
                // Fehlerbehandlung
            }
            serverSocket = tmp;
        }

        public void run() {
            BluetoothSocket socket;
            while (true) {
                try {
                    socket = serverSocket.accept();
                } catch (IOException e) {
                    break;
                }
                if (socket != null) {
                    // Verwalten Sie die Verbindung in einem separaten Thread.
                    manageConnectedSocket(socket);
                    try {
                        serverSocket.close();
                    } catch (IOException e) {
                        // Fehlerbehandlung
                    }
                    break;
                }
            }
        }

        // Schließt den Server-Socket
        public void cancel() {
            try {
                serverSocket.close();
            } catch (IOException e) {
                // Fehlerbehandlung
            }
        }
    }

    // Client-Thread, um eine Verbindung mit einem anderen Gerät herzustellen
    private class ConnectThread extends Thread {
        private final BluetoothSocket socket;

        public ConnectThread(BluetoothDevice device) {
            BluetoothSocket tmp = null;
            try {
                tmp = device.createRfcommSocketToServiceRecord(myUUID);
            } catch (IOException e) {
                // Fehlerbehandlung
            }
            socket = tmp;
        }

        public void run() {
            bluetoothAdapter.cancelDiscovery();
            try {
                socket.connect();
                manageConnectedSocket(socket);
            } catch (IOException e) {
                // Verbindungsversuch fehlgeschlagen, schließen Sie den Socket
                try {
                    socket.close();
                } catch (IOException closeException) {
                    // Fehlerbehandlung
                }
            }
        }

        // Schließt den Client-Socket
        public void cancel() {
            try {
                socket.close();
            } catch (IOException e) {
                // Fehlerbehandlung
            }
        }
    }

    // Verwaltet eine bestehende Bluetooth-Verbindung
    private void manageConnectedSocket(BluetoothSocket socket) {
        // Datenübertragung oder weitere Verarbeitung
    }
}
