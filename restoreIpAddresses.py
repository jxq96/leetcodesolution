class Solution:
    def restoreIpAddresses(self, s: str) -> [str]:
        if len(s) > 12 or len(s) < 4:
            return []
        else:
            return self.recur(4, s)

    def recur(self, remains: int, s: str) -> [str]:
        if remains > len(s) or len(s) > 3*remains:
            return []
        else:
            if remains == 1:
                if len(s) > 1 and s[0] == "0" or int(s) > 255:
                    return []
                else:
                    return [s]
            else:
                res = []
                for i in range(1, 4):
                    tmp = s[0:i]
                    if len(tmp) >= 2 and tmp[0] == "0":
                        continue
                    if int(tmp) <= 255:
                        tmpres = self.recur(remains-1, s[i:])
                        #j = 0
                        #while j < len(tmpres):
                         #   if len(tmpres[j]) > 1 and tmpres[j][0] == "0":
                          #      tmpres.pop(j)
                           # j += 1
                        if len(tmpres) != 0:
                            for j in tmpres:
                                res.append(tmp+"."+j)
                    else:
                        break
                return res