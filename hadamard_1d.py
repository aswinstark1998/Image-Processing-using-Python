import math

N = int(input("Enter Number: "))
if N%2!=0:
    print("Cannot Proceed..!!")
    exit(-1)
def findBinary(num):
    t_num = num
    bin = str("")
    if t_num==0:
        bin =str("0")
    while t_num!=0:
        d = t_num%2
        if d==0:
            bin = bin+ str("0")
        if d==1:
            bin = bin+ str("1")
        t_num = int(t_num/2)
    bin = bin+"0000000"
    return bin

def findInnerSum(u, x, N):
    if N==4:
       # print("Yeah n is 2!")
        n=2
    if N==2:
       # print("Yeah n is 1")
        n=1
    if N==8:
        n = 3
    sum =0.0;
    b_u= str("")
    b_x= str("")
    for v in range(0, n):
        b_u = findBinary(u)
        b_x = findBinary(x)
        sum = sum + (float(b_u[v])*float(b_x[v]))
    return sum

f = []
for i in range(0, N):
    f.append(int(input()))

H = []

for u in range(0, N):
    ans = 0.0
    for x in range(0, N):
        innerSum = float(findInnerSum(u, x, N))
        ans = ans+math.pow(-1, innerSum)*f[x]
    H.append(ans*math.sqrt(1.0/N))
print(H)