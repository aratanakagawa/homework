L=[[1, '英語', 25], [1, '国語', 63], [1, '数学', 42], [2, '地歴', 90], [2, '英語', 44], [3, '数学', 94]]
#科目はL[i][1]
#print(L[0][1])

def heikin(L):
    n=len(L)
    S=[]
    R=[]
    for i in range(0,n):
            S.append(L[i][1])
    S=list(set(S))

    for sub in S:
        score=0
        count=0
        for j in range(0,n):
            print(sub)
            if sub==L[j][1]:
                score = score + int(L[j][2])
                count=count+1
        #print(count)
        #print(score)
        R.append(sub)
        R.append(score/count)

    return R

print(heikin(L))

#最大値
def maxscore(L):
    n=len(L)
    S=[]
    R=[]
    for i in range(0,n):
            S.append(L[i][1])
    S=list(set(S))

    for sub in S:
        count=0
        max=0
        for j in range(0,n):
            if sub==L[j][1] and int(L[j][2])>max:
                max=int(L[j][2])
        R.append(sub)
        R.append(max)

    return R
print(maxscore(L))

#最小値
def minscore(L):
    n=len(L)
    S=[]
    R=[]
    for i in range(0,n):
            S.append(L[i][1])
    S=list(set(S))

    for sub in S:
        count=1
        min=0
        for j in range(0,n):
            if count==1 and sub==L[j][1]:
                min=int(L[j][2])
                count += 1
            if count==2 and sub==L[j][1] and int(L[i][2])<min:
                min=int(L[j][2])

        R.append(sub)
        R.append(min)

    return R
print(minscore(L))

#番号ごとの平均点
def heikin_by_number(L):
    n=len(L)
    S=[]
    R=[]
    for i in range(0,n):
            S.append(L[i][0])
    S=list(set(S))

    for num in S:
        score=0
        count=0
        for j in range(0,n):
            if num==L[j][0]:
                score = score + int(L[j][2])
                count=count+1
        #print(count)
        #print(score)
        R.append(num)
        R.append(score/count)

    return R

print(heikin_by_number(L))
