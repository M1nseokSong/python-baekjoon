import sys
input = sys.stdin.readline
n = int(input())
stack = list()
oh_big = [-1]*n
array = list(map(int, input().split()))
for _ in range(n):
    while stack and (array[stack[-1]] < array[_]):
        tmp = stack.pop()
        oh_big[tmp] = array[_]
    stack.append(_)
print(*oh_big)
