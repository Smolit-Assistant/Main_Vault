import java.util.HashSet;
import java.util.Set;

public class ClusterManager {

    private Set<ClusterNode> nodes;
    private TaskScheduler taskScheduler;

    public ClusterManager() {
        nodes = new HashSet<>();
        taskScheduler = new TaskScheduler();
    }

    // Fügt einen neuen Node zum Cluster hinzu
    public void addNode(ClusterNode newNode) {
        nodes.add(newNode);
        // Weitere Initialisierung und Konfiguration des neuen Nodes
    }

    // Entfernt einen Node aus dem Cluster
    public void removeNode(ClusterNode node) {
        nodes.remove(node);
        // Bereinigung und eventuelles Umschichten von Aufgaben
    }

    // Findet einen Node im Cluster
    public ClusterNode findNodeById(String nodeId) {
        for (ClusterNode node : nodes) {
            if (node.getId().equals(nodeId)) {
                return node;
            }
        }
        return null; // oder eine passende Exception werfen
    }

    // Verteilt eine Aufgabe an verfügbare Nodes
    public void distributeTask(Task task) {
        Set<ClusterNode> availableNodes = getAvailableNodes();
        taskScheduler.scheduleTask(task, availableNodes);
        // Weitere Logik zur Verteilung und Ausführung der Aufgabe
    }

    // Ermittelt verfügbare Nodes
    private Set<ClusterNode> getAvailableNodes() {
        Set<ClusterNode> availableNodes = new HashSet<>();
        for (ClusterNode node : nodes) {
            if (node.isAvailable()) {
                availableNodes.add(node);
            }
        }
        return availableNodes;
    }
}

class ClusterNode {
    private String id;
    private boolean available;

    public ClusterNode(String id) {
        this.id = id;
        this.available = true;
    }

    public String getId() {
        return id;
    }

    public boolean isAvailable() {
        return available;
    }

    // Weitere Methoden und Eigenschaften
}

class Task {
    private String taskId;
    // Weitere Eigenschaften und Methoden

    public Task(String taskId) {
        this.taskId = taskId;
    }

    // Weitere Methoden
}

class TaskScheduler {
    public void scheduleTask(Task task, Set<ClusterNode> nodes) {
        // Logik zur Zuweisung der Task an Nodes
    }
}
