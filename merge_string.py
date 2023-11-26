class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x=len(word1)
        y= len(word2)
        z=""
        if len(word1)>len(word2):
            for i in range(x):
                z+=word1[i]
                if i<y:
                    z+=word2[i]
        else:
            for j in range(y):
                if j<x:
                    z+=word1[j]
                z+=word2[j]
        return z
