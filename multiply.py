class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        else:
            num1 = num1[::-1]
            num2 = num2[::-1]
            tmp = [0 for _ in range(len(num2) + len(num1))]
            for i in range(len(num1)):
                for j in range(len(num2)):
                    tmp[i + j] += int(num1[i]) * int(num2[j])
            lenth = len(tmp)
            ans = []
            for i in range(len(tmp)):
                a = tmp[i] // 10
                b = tmp[i] % 10
                if i < lenth - 1:
                    tmp[i + 1] += a
                ans.insert(0, str(b))
            while ans[0] == "0":
                ans.pop(0)
            return "".join(ans)