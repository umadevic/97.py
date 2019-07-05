uma1=int(input())
san1=list(map(int,input().split()))
for p in range(len(san1)-1):
     if(san1[p]>san1[p+1]):
           print(p)
           break
