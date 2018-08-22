class Solution:
    def split(self, string, width):
        result = []
        i = 0
        length = len(string)
        while i <= length - width:
            result.append(string[i:i + width])
            i = i + width
        return result

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        words_count = len(words)
        if words_count > 0:
            length_word = len(words[0])
        else:
            length_word = 0
        i = 0
        length_s = len(s)
        words.sort()
        if length_s == 0 or words_count == 0:
            return []
        threshold = length_s - length_word * words_count
        step = length_word*words_count
        while i <= threshold:
            string_list = sorted(self.split(
                s[i:i + step], length_word))
            if string_list == words:
                result.append(i)
            i = i + 1
        return result
