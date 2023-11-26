class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        a=1
        while True:
            n=a*n
            if n%2==0:
                return n
            else:
                a+=1 
        
