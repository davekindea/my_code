class Solution:
    def reverse(self, x: int) -> int:
        y=str(x)
        if y[0]=="-":
            x=y[1:]
            z=int("-"+x[::-1])
        else:
            z=int(y[::-1])
        a=2147483647
        b=(-2147483648)
        if z>=a or z<=b:
            return 0
        else:
            return z
        
        
