class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            b=1
        else:
            b=0
            for i in range (len(s)):
                x=[]
                y=s[i]
                x.append(y)
                a=1
                for j in range (i+1,len(s)):
                    z=s[j]
                    if z not in x:
                        x.append(z)
                        a+=1
                        if b<a:
                            b=a
                    else:
                        if b<a:
                            b=a
                        break
        return b
