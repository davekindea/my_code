class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        y=""
        x=0
        for i in range (len(spaces)):
                y+=(s[x:spaces[i]]+" ")
                x=spaces[i]
        if (len(s))==spaces[len(spaces)-1]:
            y+=(s[x:(len(s))]+" ")
        else:
            y+=s[x:(len(s))]
        return y


        
