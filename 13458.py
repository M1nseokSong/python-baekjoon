import sys
input = sys.stdin.readline
n = int(input())
exam = list(map(int, input().split()))
b, c = map(int, input().split())
result = 0
for i in exam:
    i -= b
    if i <= 0:
        result += 1
        continue
    tmp = i // c
    result += (1 + tmp)
    if i % c > 0:
        result += 1
print(result)
    
