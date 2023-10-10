n=int(input())
for i in range (n):
    x=int(input())
    arr=list(map(int,input().strip().split()))
    arr.sort()
    if x==1:
        print("YES")
    else:
        a=0
        for j in range (x-1):
                c=arr[j+1]-arr[j]
                if c>=a:
                    a=c
        if a>1:
            print("NO")
        else:
            print("YES")
