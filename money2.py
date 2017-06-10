coin = [500,100,50,10,1]
input_money=int(input("金額は？"))

for i in coin:
  if input_money % i == 0:
    print(int(input_money/i))
    break

  else:
    print(int(input_money/i))
    input_money=input_money % i
    
