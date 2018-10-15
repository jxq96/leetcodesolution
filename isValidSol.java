public class isValidSol {
    public static boolean isValid(String s) {
        Stack < Character > stack = new Stack < > ();
        if (s == null || s.length() == 0) {
            return true;
        } else {
            int len = s.length();
            for (int i = 0; i < len; i++) {
                if (!stack.isEmpty() && ismatch(s.charAt(i), stack.peek().charValue())) {
                    stack.pop();
                } else {
                    stack.push(s.charAt(i));
                }
            }
            return stack.isEmpty();

        }
    }
    static boolean ismatch(char a, char b) {
        switch (a) {
            case '{':
                return b == '}';
            case '}':
                return b == '{';
            case '(':
                return b == ')';
            case ')':
                return b == '(';
            case '[':
                return b == ']';
            case ']':
                return b == '[';
            default:
                return true;
        }
    }
}