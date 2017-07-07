def sorted(L):
    n=len(L[1])

    for i in range(0,n): #n=0,1,2,3,4
        min=i

        for j in range(i+1,n): #現時点で一番左にある小さい数字と、それよりも右にある数を比べる
            if L[1][min]>L[1][j]:
                min=j #もし右にある数字が大きければ位置番号minを入れ替える
                #minは2

        for k in range(0, 2): #range(開始値,終了値)の終了値は+1の数字を入れる
            tmp = L[k][min]
            L[k][min] = L[k][i]
            L[k][i] = tmp

        #temp=L[i][i]
        #L[i][i]=L[min][min]
        #L[min][min]=temp

    return L


M=([ ['田中', '山下', '中村', '村上', '江口'],[    35,    69,     21,     12,    46]])
sorted(M)
print(M)
