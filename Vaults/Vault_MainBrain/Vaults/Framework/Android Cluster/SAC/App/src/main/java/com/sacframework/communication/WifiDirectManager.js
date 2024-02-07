import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.net.wifi.p2p.WifiP2pConfig;
import android.net.wifi.p2p.WifiP2pManager;
import android.net.wifi.p2p.WifiP2pManager.Channel;
import android.net.wifi.p2p.WifiP2pManager.PeerListListener;
import android.net.wifi.p2p.WifiP2pManager.ConnectionInfoListener;
import android.net.wifi.p2p.WifiP2pDeviceList;
import android.net.wifi.p2p.WifiP2pDevice;
import android.net.wifi.p2p.WifiP2pInfo;

public class WifiDirectManager {

    private WifiP2pManager manager;
    private Channel channel;
    private BroadcastReceiver receiver;
    private IntentFilter intentFilter;
    private Context context;
    private PeerListListener peerListListener;
    private ConnectionInfoListener connectionInfoListener;

    public WifiDirectManager(Context context) {
        this.context = context;

        // Initialisiert WiFi P2P Manager und Channel
        manager = (WifiP2pManager) context.getSystemService(Context.WIFI_P2P_SERVICE);
        channel = manager.initialize(context, context.getMainLooper(), null);

        // Intent-Filter für WiFi P2P Events
        intentFilter = new IntentFilter();
        intentFilter.addAction(WifiP2pManager.WIFI_P2P_STATE_CHANGED_ACTION);
        intentFilter.addAction(WifiP2pManager.WIFI_P2P_PEERS_CHANGED_ACTION);
        intentFilter.addAction(WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION);
        intentFilter.addAction(WifiP2pManager.WIFI_P2P_THIS_DEVICE_CHANGED_ACTION);

        // PeerListListener und ConnectionInfoListener
        setupListeners();

        // BroadcastReceiver für die Handhabung von WiFi P2P Events
        receiver = new WiFiDirectBroadcastReceiver(manager, channel, peerListListener, connectionInfoListener);
    }

    // Startet die Entdeckung von Peers
    public void discoverPeers() {
        manager.discoverPeers(channel, new WifiP2pManager.ActionListener() {
            @Override
            public void onSuccess() {
                // Peer-Entdeckung gestartet
            }

            @Override
            public void onFailure(int reason) {
                // Fehler bei der Peer-Entdeckung
            }
        });
    }

    // Verbindet mit einem bestimmten Peer
    public void connect(WifiP2pDevice device) {
        WifiP2pConfig config = new WifiP2pConfig();
        config.deviceAddress = device.deviceAddress;
        manager.connect(channel, config, new WifiP2pManager.ActionListener() {
            @Override
            public void onSuccess() {
                // Verbindungsaufbau gestartet
            }

            @Override
            public void onFailure(int reason) {
                // Fehler beim Verbindungsaufbau
            }
        });
    }

    private void setupListeners() {
        peerListListener = new WifiP2pManager.PeerListListener() {
            @Override
            public void onPeersAvailable(WifiP2pDeviceList peerList) {
                // Verfügbarkeit der Peers behandeln
            }
        };

        connectionInfoListener = new WifiP2pManager.ConnectionInfoListener() {
            @Override
            public void onConnectionInfoAvailable(WifiP2pInfo info) {
                // Verbindungsinformationen behandeln
            }
        };
    }

    // Registriert den BroadcastReceiver
    public void registerReceiver() {
        context.registerReceiver(receiver, intentFilter);
    }

    // Deregistriert den BroadcastReceiver
    public void unregisterReceiver() {
        context.unregisterReceiver(receiver);
    }
}

class WiFiDirectBroadcastReceiver extends BroadcastReceiver {

    private WifiP2pManager manager;
    private Channel channel;
    private PeerListListener peerListListener;
    private ConnectionInfoListener connectionInfoListener;

    public WiFiDirectBroadcastReceiver(WifiP2pManager manager, Channel channel, 
                                       PeerListListener peerListListener,
                                       ConnectionInfoListener connectionInfoListener)
