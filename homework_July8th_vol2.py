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
                #http://www.lifewithpython.com/2015/05/python-dict-default-value.html
                counts[x[1]]=counts.get(x[1],0)+1
                score[x[1]]=score.get(x[1],0)+x[2]

    average={i:score[i]/j for i,j in counts.items()}


    return average

print(heikin(L))

#-------------------------
#科目ごとの最大値
def maxscore(L):
    maxL=dict()
    for x in L:
                if not x[1] in maxL or maxL[x[1]] < x[2]:
                    maxL[x[1]]=x[2]
    return maxL

print(maxscore(L))

#-------------------------
#科目ごとの最低値
def minscore(L):
    minL=dict()
    for x in L:
                if not x[1] in minL or minL[x[1]] > x[2]:
                    minL[x[1]]=x[2]
    return minL

print(minscore(L))

#-------------------------
#番号ごとの平均点
def average(L):
    counts=dict()
    score=dict()
    avg=dict()
    for x in L:
                counts[x[0]]=counts.get(x[0],0)+1
                score[x[0]]=score.get(x[0],0)+x[2]

    avg={i:score[i]/j for i,j in counts.items()}

    return avg

print(average(L))

#-------------------------
