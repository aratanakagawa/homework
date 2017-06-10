yen = int(input("金額を入力してください"))
count_500=0
count_100=0
count_50=0
count_10=0
count_1=0


while yen / 500 >= 1:
  count_500 += 1
  yen = yen - 500

while yen/100 >=1:
  count_100 +=1
  yen = yen - 100

while yen/50 >=1:
  count_50 +=1
  yen = yen - 50

while yen/10 >=1:
  count_10 +=1
  yen = yen - 10

  while yen/1 >=1:
    count_1 +=1
    yen = yen - 1


print(count_500)
print(count_100)
print(count_50)
print(count_10)
print(count_1)
