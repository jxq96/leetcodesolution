class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[len(digits)-1] += 1
        if digits[len(digits) - 1] < 10 :
            return digits
        for i in reversed(range(len(digits))):
            if digits[i] == 10:
                digits[i] = 0
                if i > 0:
                    digits[i-1] += 1
                    if digits[i-1] < 10:
                        break
                else:
                    digits.insert(0, 1)
        return digits
