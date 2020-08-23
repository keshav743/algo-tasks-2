n = int(input())
q = int(input())
arr = []
nCount = 0

if((n>=1 and n<=pow(10,18)) and (q>=1 and q<=pow(10,5))):
    for i in range(1,n+1):
        arr.append(i)

    while(nCount<q):
        l,r,v = input().split()
        for i in range(int(l),int(r)+1):
            arr[i-1]+=int(v)
        nCount+=1
    
    print(max(arr))                
