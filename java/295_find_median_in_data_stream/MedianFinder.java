class MedianFinder {
    private PriorityQueue<Integer> maxheap;
    private PriorityQueue<Integer> minheap;
    private int count;

    public MedianFinder() {
        this.maxheap = new PriorityQueue<>(Comparator.reverseOrder());
        this.minheap = new PriorityQueue<>(Comparator.naturalOrder());
        this.count = 0;
    }
    
    public void addNum(int num) {
        if (this.maxheap.isEmpty() || num < this.maxheap.peek()) {
            this.maxheap.offer(num);
        } else {
            this.minheap.offer(num);
        }

        this.count++;

        // rebalance
        if (this.maxheap.size() > this.minheap.size() + 1) {
            this.minheap.offer(this.maxheap.poll());
        } else if (this.minheap.size() > this.maxheap.size()) {
            this.maxheap.offer(this.minheap.poll());
        }
    }
    
    public double findMedian() {
        if (this.count % 2 == 1) {
            return (double) this.maxheap.peek();
        }

        return (double) (this.maxheap.peek() + this.minheap.peek()) / 2;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */