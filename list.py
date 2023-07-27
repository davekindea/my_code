if __name__ == '__main__':
    N = int(input())
z=[]
for i in range (N):
    x=input()
    if x=="print":
        print(z)
    elif x[:6]=="insert":
        z.insert(int(x[7:8]),int(x[9:]))
    elif x[:6]=="remove":
        z.remove(int(x[7:]))
    elif x[:6]=="append":
        z.append(int(x[7:]))
    elif x=="sort":
        z.sort()
    elif x=="pop":
        z.pop()
    else:
        z.reverse()
        
        
        
