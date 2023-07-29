class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        if len(s)==1:
            return True
        else:
            for i in range (len(s)):
                y=ord(s[i])
                if y>=97 and y<=122:
                    x+=s[i]
                elif y>=48 and y<=57:
                    x+=s[i]
                elif y>=65 and y<=90:
                    x=x+s[i].lower()
                else:
                    continue
            a=len(x)-1
            z=x[::-1]
            for j in range (len(x)):
                if x[j]==z[j]:
                    continue
                else:
                    return False
                    break
            else:
                return True
        
