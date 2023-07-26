class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        x=[]
        intervals.sort()
        for i in intervals:
            if len(x)==0 or x[-1][1] < i[0]:
                x.append(i)
            else:
                x[-1][1] = max(x[-1][1],i[1])
            
        return x
