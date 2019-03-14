class Solution:
    def recur(self,s1: str, s2: str, s3:str) -> bool:
        if len(s1) == 0:
            return s2 == s3
        elif len(s2) == 0:
            return s1 == s3
        else:
            t1 = s1[0]
            t2 = s2[0]
            t3 = s3[0]
            if t1 == t2:
                if t1 == t3:
                    return self.recur(s1[1:], s2, s3[1:]) or self.recur(s1,s2[1:],s3[1:])
                else:
                    return False
            elif t1 == t3:
                return self.recur(s1[1:], s2, s3[1:])
            elif t2 == t3:
                return self.recur(s1, s2[1:], s3[1:])
            else:
                return False

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        else:
            return self.recur(s1, s2, s3)