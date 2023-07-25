class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum=0
        for i in range (len(chalk)):
            sum+=chalk[i]
        y=k%sum
        a=0
        for j in range (len(chalk)):
                y=y-chalk[j]
                if y>=0:
                    continue
                else:
                    a=j
                    break
        return a
