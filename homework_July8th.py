L=[[1, '英語', 25], [1, '国語', 63], [1, '数学', 42], [2, '地歴', 90], [2, '英語', 44], [3, '数学', 94]]
#科目はL[i][1]
#print(L[0][1])

#-------------------------
#科目ごとの平均点
def heikin(L):
    counts=dict()
    score=dict()
    average=dict()
    for x in L:
        for y in x:
            if x.index(y)==1:
                #http://www.lifewithpython.com/2015/05/python-dict-default-value.html
                counts[y]=counts.get(y,0)+1
                score[y]=score.get(y,0)+x[2]

    for i,j in counts.items():
        average[i]=score[i]/j

    return average

print(heikin(L))

#-------------------------
#科目ごとの最大値
def maxscore(L):
    MAXL=dict()
    for x in L:
        for y in x:
            if x.index(y)==1:
                if not y in MAXL or MAXL[y] < x[2]:
                    MAXL[y]=x[2]
    return MAXL

print(maxscore(L))

#-------------------------
#科目ごとの最低値
def minscore(L):
    MINL=dict()
    for x in L:
        for y in x:
            if x.index(y)==1:
                if not y in MINL or MINL[y] > x[2]:
                    MINL[y]=x[2]
    return MINL

print(minscore(L))

#-------------------------
#番号ごとの平均点
def average(L):
    counts=dict()
    score=dict()
    avg=dict()
    for x in L:
        for y in x:
            if x.index(y)==0:
                counts[y]=counts.get(y,0)+1
                score[y]=score.get(y,0)+x[2]

    for i,j in counts.items():
        avg[i]=score[i]/j

    return avg

print(average(L))

#-------------------------
