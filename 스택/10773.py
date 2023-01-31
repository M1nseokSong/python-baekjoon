k = int(input())
coins = list()
for _ in range(k):
    tmp = int(input())
    if tmp != 0:
        coins.append(tmp)
    else:
        coins.pop()
print(sum(coins))
