import org.junit.Test;
import static org.junit.Assert.*;

public class DataManagerNetworkIntegrationTest {

    private DataManager dataManager;
    private NetworkHelper networkHelper;

    @Before
    public void setUp() {
        networkHelper = new NetworkHelper(); // Angenommen, dieser stellt Netzwerkfunktionen bereit
        dataManager = new DataManager(networkHelper); // DataManager nutzt NetworkHelper
    }

    @Test
    public void fetchData_fromNetwork_dataIsCorrectlyStored() {
        String testData = "Testdaten aus dem Netzwerk";
        // Simulieren, dass NetworkHelper Daten vom Netzwerk lädt
        when(networkHelper.fetchDataFromNetwork()).thenReturn(testData);

        dataManager.fetchAndStoreData();

        // Überprüfen, ob die Daten korrekt im DataManager gespeichert wurden
        assertEquals(testData, dataManager.getStoredData());
    }

    // Weitere Integrationstests für andere Interaktionen
}

// Mock-Klassen oder Mocking-Frameworks können verwendet werden, um Abhängigkeiten zu simulieren
