class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            a=list(s)
            b=list(t)
        
            for i in range(len(s)):
                if a[i] in b :
                    b.remove(a[i])
                    continue
                else:
                    return False
            else:
                return True
