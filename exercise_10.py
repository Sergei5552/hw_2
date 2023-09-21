coins = int(input("Введите количество монет: "))
heads = 0
tails = 0
for i in range(coins):
    heads_or_tails = int(input("Если орёл введите 1, если решка введите 0: "))
    if heads_or_tails == 1:
        heads += 1
    else: tails += 1
if heads < tails:
    print(f'Переверните {heads} монет которые к вам орлом')
else: print(f'Переверните {tails} монет которые к вам решкой')