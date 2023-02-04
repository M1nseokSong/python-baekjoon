n = int(input())
time_get_money = list(map(int, input().split()))
result = 0
time_get_money.sort()
for _ in range(n):
    result += sum(time_get_money[0:_+1])
print(result)
