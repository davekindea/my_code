class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        x={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        a=0
        b=0
        for i in range (len(num1)):
            z=x.get(num1[i])
            a=a+z*(10**(len(num1)-1-i))
        for j in range (len(num2)):
            y=x.get(num2[j])
            b=b+y*(10**(len(num2)-1-j))
        return str(a*b)
        
        
