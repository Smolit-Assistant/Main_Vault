import java.util.Set;
import java.util.Queue;
import java.util.LinkedList;
import java.util.HashMap;
import java.util.Map;

public class TaskScheduler {

    private Queue<Task> taskQueue;
    private Map<String, ClusterNode> nodes;

    public TaskScheduler() {
        taskQueue = new LinkedList<>();
        nodes = new HashMap<>();
    }

    // Fügt einen neuen Node zum Scheduler hinzu
    public void addNode(ClusterNode node) {
        nodes.put(node.getId(), node);
    }

    // Entfernt einen Node aus dem Scheduler
    public void removeNode(String nodeId) {
        nodes.remove(nodeId);
    }

    // Fügt eine neue Aufgabe zur Warteschlange hinzu
    public void scheduleTask(Task task) {
        taskQueue.add(task);
        processTasks();
    }

    // Verarbeitet die Aufgaben in der Warteschlange
    private void processTasks() {
        while (!taskQueue.isEmpty()) {
            Task task = taskQueue.poll();
            ClusterNode bestNode = findBestNodeForTask(task);
            if (bestNode != null) {
                bestNode.assignTask(task);
            } else {
                // Kein verfügbarer Node, Aufgabe zurück in die Warteschlange
                taskQueue.add(task);
                break;
            }
        }
    }

    // Findet den besten Node für eine gegebene Aufgabe
    private ClusterNode findBestNodeForTask(Task task) {
        for (ClusterNode node : nodes.values()) {
            if (node.isAvailable() && node.hasCapacityForTask(task)) {
                return node;
            }
        }
        return null;
    }
}

class ClusterNode {
    private String id;
    private boolean available;
    private int capacity; // Kapazität des Nodes für Aufgaben

    public ClusterNode(String id, int capacity) {
        this.id = id;
        this.available = true;
        this.capacity = capacity;
    }

    public String getId() {
        return id;
    }

    public boolean isAvailable() {
        return available;
    }

    public boolean hasCapacityForTask(Task task) {
        // Logik zur Überprüfung, ob der Node die Aufgabe ausführen kann
        return task.getRequiredCapacity() <= capacity;
    }

    public void assignTask(Task task) {
        // Zuweisung der Aufgabe an den Node
        capacity -= task.getRequiredCapacity();
        // Weitere Logik zur Aufgabenverarbeitung
    }

    // Weitere Methoden und Eigenschaften
}

class Task {
    private String taskId;
    private int requiredCapacity;

    public Task(String taskId, int requiredCapacity) {
        this.taskId = taskId;
        this.requiredCapacity = requiredCapacity;
    }

    public int getRequiredCapacity() {
        return requiredCapacity;
    }

    // Weitere Methoden
}
