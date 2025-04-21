class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> mins;

    public MinStack() {
        this.stack = new Stack<>();
        this.mins = new Stack<>();
    }
    
    public void push(int val) {
        if (this.mins.size() == 0 || this.mins.peek() >= val) {
            this.mins.push(val);
        }
        this.stack.push(val);
    }
    
    public void pop() {
        if (this.mins.size() > 0 && this.mins.peek().equals(this.stack.peek())) {
            this.mins.pop();
        }
        this.stack.pop();
    }
    
    public int top() {
        return this.stack.peek();
    }
    
    public int getMin() {
        return this.mins.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */