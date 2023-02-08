import sys
input = sys.stdin.readline
n, s = map(int, input().split())
array = list(map(int, input().split()))
start, end = 0, 0
result = 100001
for i in range(1, n):
    array[i] = array[i] + array[i-1]
while(end!=n):
    if start == 0:
        tmp_sum = array[end]
    else:
        tmp_sum = array[end] - array[start-1]
    if tmp_sum >= s:
        if end+1-start <= result:
            result = end+1-start
        start += 1
    else:
        end += 1

print(result if result != 100001 else 0)
