# 구간 합 구하기 4
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [0] + list(map(int, input().split()))

# 누적 합
for _ in range(1, n+1):
    array[_] = array[_] + array[_-1]

for _ in range(m):
    start, end = map(int, input().split())
    print(array[end]-array[start-1])
