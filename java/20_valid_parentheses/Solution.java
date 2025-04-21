class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Set<Character> openType = new HashSet<>(Arrays.asList('(', '{','['));
        for (char c: s.toCharArray()) {
            if (openType.contains(c)) {
                stack.push(c);
            } else {
                boolean matched = !stack.isEmpty() && (
                    (c == ')' && stack.peek() == '(') ||
                    (c == '}' && stack.peek() == '{') ||
                    (c == ']' && stack.peek() == '[')
                );
                if (matched) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}