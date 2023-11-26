class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        y=[]
        for i in range(left,right+1):
            x=str(i)
            if "0" in x:
                pass
            else:
                for j in range(len(x)):
                    if i%int(x[j])==0:
                        continue
                    else:
                        break
                else:
                    y.append(i)
        return y
