import sys
n=int(raw_input())
a=0
g=0
while(n>0):
    r=raw_input().split()
    r[0]=int(r[0])
    r[1]=int(r[1])
    if(g+r[0]-a<=500):
        g+=r[0]
        sys.stdout.write("A")
    else:
        a+=r[1]
        sys.stdout.write("G")
    n-=1
