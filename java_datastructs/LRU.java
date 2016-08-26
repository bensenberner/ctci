import java.util.HashMap;

// front = MRU
// back = LRU

class LRU {
    private HashMap<String, Node> dict;
    private Node head;
    private Node tail;
    private int capacity;

    class Node {
        private int value;
        private Node nextNode;
        private Node prevNode;

        public Node(int value) {
            this.value = value;
            this.nextNode = null;
            this.prevNode = null;
        }

        public void setValue(int value) {
            this.value = value;
        }

        public int getValue() {
            return this.value;
        }
    }

    public LRU(int capacity) {
        this.capacity = capacity;
        this.dict = new HashMap<String, Node>();
        this.head = null;
        this.tail = null;
    }

    private Node getNode(String key) {
        return this.dict.get(key);
    }

    private int getVal(String key) {
        Node node = getNode(key);
        if (node != null) {
            return node.getValue();
        } else { // correct behaviour?
            return 0;
        }
    }

    private void put(String key, int value) {
        if (this.dict.containsKey(key)) {
            Node oldNode = this.dict.get(key);
            if (oldNode != null) {
                oldNode.setValue(value);
                removeFromList(oldNode);
                addFront(oldNode);
            } else {
                Node newNode = new Node(value);
                this.dict.put(key, newNode);
                addFront(newNode);
            }

        } else { // must create a new Node
            Node newNode = new Node(value);
            if (this.dict.size() < this.capacity) {
                // add to the front
                this.dict.put(key, newNode);
                addFront(newNode);
            } else { // need to remove the LRU before adding a new one
                evictLRU();
                addFront(newNode);
            }
        }
    }

    private Node evictLRU() {

    }
}
