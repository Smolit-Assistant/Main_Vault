## Smolit-Androit-Cluster

Das SAC-Framework ist eine speziell entwickelte Softwarelösung, die darauf abzielt, Android-Geräte in einem Cluster zu verbinden und zu verwalten. Es ermöglicht die gemeinsame Nutzung von Ressourcen und die verteilte Ausführung von Aufgaben zwischen diesen Geräten. Das Framework besteht aus mehreren Hauptmodulen:

### 1. **Kernmodul:** 
Beinhaltet Kernfunktionen wie `ClusterManager` und `DeviceManager` zur Verwaltung des Clusters und der einzelnen Geräte.
### 2. **Kommunikationsmodul:** 
Stellt die Verbindung zwischen den Geräten über verschiedene Methoden (WiFi, Bluetooth, USB) sicher und enthält Klassen wie `WifiDirectManager`, `BluetoothManager` und `USBConnectionManager`.
### 3. **Sicherheitsmodul:**
Verantwortlich für Authentifizierung, Autorisierung und Datenverschlüsselung mit Komponenten wie `AuthenticationManager`, `AuthorizationManager` und `EncryptionManager`.
### 4. **Datenmanagementmodul:**
Managt die Datenspeicherung und -synchronisation mit Komponenten wie `DataManager` und `FileSyncManager`.
### 5. **Benutzeroberflächenmodul:**
Beinhaltet UI-Komponenten wie `MainUIController`, `NodeUIController` und `TaskUIController` zur Interaktion mit dem Benutzer.
    
### 6. **Hilfsmodul:**
Bietet unterstützende Funktionen wie Logging (Logger) und Konfigurationsmanagement (ConfigManager). 
### 7. **Testmodul:** 
Umfasst Testkomponenten für Unit-Tests, Integrationstests und UI-Automatisierungstests.


## Dateien, für die noch Beispielcode erstellt werden muss:

[ChatGPT ChatLink](https://chat.openai.com/share/5ea6ad07-efa8-4557-a360-0eaf030f255a) 

1. **Ressourcen-Modul (res/):**
    - Layouts (z.B. activity_main.xml, activity_node_ui.xml, activity_task_ui.xml)
    - Values (z.B. strings.xml, styles.xml, colors.xml)

1. **Weitere Dateien in der Dokumentation (docs/):**
    - architecture.md
    - api_reference.md
    - user_guide.md
## SAC-Framework
Textuelle Ordnerstruktur des SAC-Frameworks (Smolit-Android-Cluster):

SAC-Framework/
│
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   ├── com/
│   │   │   │   ├── sacframework/
│   │   │   │   │   ├── core/
│   │   │   │   │   │   ├── ClusterManager.java
│   │   │   │   │   │   ├── DeviceManager.java
│   │   │   │   │   │   └── TaskScheduler.java
│   │   │   │   │   ├── communication/
│   │   │   │   │   │   ├── WifiDirectManager.java
│   │   │   │   │   │   ├── BluetoothManager.java
│   │   │   │   │   │   └── USBConnectionManager.java
│   │   │   │   │   ├── security/
│   │   │   │   │   │   ├── AuthenticationManager.java
│   │   │   │   │   │   ├── AuthorizationManager.java
│   │   │   │   │   │   └── EncryptionManager.java
│   │   │   │   │   ├── data/
│   │   │   │   │   │   ├── DataManager.java
│   │   │   │   │   │   └── FileSyncManager.java
│   │   │   │   │   ├── ui/
│   │   │   │   │   │   ├── MainActivity.java
│   │   │   │   │   │   ├── NodeUIController.java
│   │   │   │   │   │   └── TaskUIController.java
│   │   │   │   │   └── utility/
│   │   │   │   │       ├── Logger.java
│   │   │   │   │       └── ConfigManager.java
│   │   │   └── ...
│   │   ├── res/
│   │   │   ├── layout/
│   │   │   │   ├── activity_main.xml
│   │   │   │   ├── activity_node_ui.xml
│   │   │   │   └── activity_task_ui.xml
│   │   │   ├── values/
│   │   │   │   ├── strings.xml
│   │   │   │   ├── styles.xml
│   │   │   │   └── colors.xml
│   │   │   └── ...
│   │   └── AndroidManifest.xml
│   └── ...
│
├── test/
│   ├── java/
│   │   ├── com/
│   │   │   ├── sacframework/
│   │   │   │   ├── unit/
│   │   │   │   │   ├── ClusterManagerTest.java
│   │   │   │   │   ├── DeviceManagerTest.java
│   │   │   │   │   └── ...
│   │   │   │   ├── integration/
│   │   │   │   │   ├── CommunicationIntegrationTest.java
│   │   │   │   │   ├── DataIntegrationTest.java
│   │   │   │   │   └── ...
│   │   │   │   └── ui/
│   │   │   │       ├── MainActivityUITest.java
│   │   │   │       ├── NodeUIControllerUITest.java
│   │   │   │       └── TaskUIControllerUITest.java
│   │   └── ...
│   └── ...
│
└── docs/                          # Dokumentation
    ├── architecture.md
    ├── api_reference.md
    └── user_guide.md
