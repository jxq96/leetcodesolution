public class generateParenthesisSol{
    public List<String> generateParenthesis(int n) {
        List<String> strings = new ArrayList<String>();
        if (n == 0) return strings;

        dfs(0, 0, "", strings, n);

        return strings;
    }

    private void dfs(int left, int right, String buffer, List<String> strings, int n) {
        if (left == n && right == n) {
            strings.add(buffer);
            return;
        }

        if (left < n) {
            dfs(left + 1, right, buffer + "(", strings, n);
        }

        if (left > right) {
            dfs(left, right + 1, buffer + ")", strings, n);
        }
    }
}