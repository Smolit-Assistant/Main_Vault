import android.app.Activity;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;
import android.view.View;

public class NodeUIController extends Activity {

    private ListView listViewNodes;
    private ArrayAdapter<String> nodesAdapter;
    private String[] nodes; // Diese Daten sollten aus dem ClusterManager geholt werden

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_node_ui_controller);

        listViewNodes = findViewById(R.id.listViewNodes);

        // Beispiel-Daten für Nodes (in der Praxis aus ClusterManager laden)
        nodes = new String[]{"Node 1", "Node 2", "Node 3"};
        nodesAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, nodes);
        listViewNodes.setAdapter(nodesAdapter);

        listViewNodes.setOnItemClickListener((parent, view, position, id) -> {
            String node = nodes[position];
            // Implementieren Sie hier die Logik, um Details für einen bestimmten Node anzuzeigen
            Toast.makeText(NodeUIController.this, "Ausgewählt: " + node, Toast.LENGTH_SHORT).show();
        });
    }

    // Weitere Methoden und UI-Interaktionen
}
