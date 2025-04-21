class Node {
    private int key;
    private int val;
    private Node next;
    private Node prev;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.next = null;
        this.prev = null;
    }

    public int getKey() {
        return this.key;
    }

    public int getVal() {
        return this.val;
    }

    public Node getNext() {
        return this.next;
    }

    public void setNext(Node next) {
        this.next = next;
    }

    public Node getPrev() {
        return this.prev;
    }

    public void setPrev(Node prev) {
        this.prev = prev;
    }

}

class LRUCache {
    private Map<Integer, Node> memo;
    private int cap;
    private Node head;
    private Node tail;

    private static void delete(Node node) {
        Node before = node.getPrev(), after = node.getNext();
        before.setNext(after);
        after.setPrev(before);
    }

    private void append(Node node) {
        Node last = this.tail.getPrev();
        last.setNext(node);
        node.setPrev(last);
        node.setNext(this.tail);
        this.tail.setPrev(node);
    }

    public LRUCache(int capacity) {
        this.memo = new HashMap<>();
        this.cap = capacity;
        this.head = new Node(-1, -1);
        this.tail = new Node(-1, -1);
        this.head.setNext(this.tail);
        this.tail.setPrev(this.head);
    }
    
    public int get(int key) {
        Node node = this.memo.get(key);
        if (null == node) {
            return -1;
        }
        LRUCache.delete(node);
        this.append(node);
        return node.getVal();
    }
    
    public void put(int key, int value) {
        Node node;
        if (this.memo.containsKey(key)) {
            node = this.memo.get(key);
            LRUCache.delete(node);
        }
        node = new Node(key, value);
        this.memo.put(key, node);

        if (this.memo.size() > this.cap) {
            Node first = this.head.getNext();
            LRUCache.delete(first);
            this.memo.remove(first.getKey());
        }

        this.append(node);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */