class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0 or s == "":
            return []
        else:
            lenth = 0
            for word in words:
                lenth = lenth + len(word)
            result = []
            lens = len(s)
            for i in range(lens):
                if self.validate(s[i:i + lenth], words.copy()):
                    result.append(i)
            return result


    def validate(self,s,words):
        if s == "" and len(words) == 0:
            return True
        elif s == "" and len(words) != 0 or s != "" and len(words) == 0:
            return False
        else:
            for word in words:
                if s.startswith(word):
                    tmp = words.copy()
                    tmp.remove(word)
                    if self.validate(s[len(word):],tmp):
                        return True
            return False