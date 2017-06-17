def square(x):
    y=x*x
    return y

v=square(6)
print(v)


def cumsum(L,l,r):
    sum=0
    for i in L[l:r]:
        sum=sum+i
    return sum

v=cumsum([1,2,3,4,5],1,3)
print(v)


def fib(n):
    li=[]
    for i in range(n):
        if i==0:
            li.append(1)
        elif i==1:
            li.append(1)
        else:
            li.append(li[i-2]+li[i-1])
    return li[n-1]

v=fib(10)
print(v)


def sorted(L):
    left=0
    right=len(L)
    i=0
    k=0
    x=0 #左側の変数
    y=0 #右側の変数
        while i<k:
            for L[i]>L[left] and i<right:
                i +=

            for L[k]<L[left] and k>left:
                k -=:

            L[i],L[k]=L[k],L[i]


        x=L[left]
        L[left]=L[k]
        L[k]=x

    return L

M=sorted([5,8,9,1,2,6,8])
print(M)
