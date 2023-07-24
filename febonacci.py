class Solution:
    def fib(self, n: int) -> int:
        
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            x0=0
            x1=1
            for i in range (2,n+1):
                
                x2=x1+x0
                x0=x1
                x1=x2
            return x2
            
