class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.my_combine(1, n, k)

    def my_combine(self, start, end, k):
        if end - start + 1 == k:
            return [[i for i in range(start, end+1)]]
        elif k == 1:
            return [[i] for i in range(start, end+1)]
        else:
            tmp = self.my_combine(start+1, end, k-1)
            for t in tmp:
                t.insert(0, start)
            tmp.extend(self.my_combine(start+1, end, k))
            return tmp