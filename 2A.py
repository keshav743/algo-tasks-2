import sys

n = int(input())
count = 0
a=[]
maxL=[]

if(n<=500):

    while(count<n):
        t=""
        x = input()
        for i in x:
            if(i == "<" or i == ">"):
                t+=i
                if(t == x):
                    a.append(t)
        count+=1
        
    for i in a:
        if(len(i)>1000000):
            sys.exit()
    
    for i in a:
        n=""
        d = []
        for j in range(1,len(i)+1):
            n=""
            for k in range(0,j):
                n+=i[k]
            d.append(n)
        maxL = []
        for s in d:
            m = ""
            if("<>" in s):
                m = s
                while("<>" in m or m == "<>"):
                    m=m.replace("<>","")
                if(m==""):    
                    maxL.append(len(s))
        if(not len(maxL) == 0):
            print(max(maxL))
        else:
            print("0")
