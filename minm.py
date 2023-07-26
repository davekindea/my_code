class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        a=0
        for i in range (len(blocks)-k+1):
            b=0
            for j in range (i,i+k):
                if blocks[j]=="B":
                    b+=1
                    if b>a:
                        a=b
                else:
                    continue
        c=k-a
        return c
