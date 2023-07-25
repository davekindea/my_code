n,m,a=map(int,input().split())
x=n//a
y=n/a
b=m//a
c=m/a
if y>x:
    x+=1
else:
    x=x
if b<c:
    b+=1
else:
    b=b
z=((x*a)*(b*a))//(a*a)
print(z)
