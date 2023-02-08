from collections import deque
import sys
int_que = deque()
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    order = input().split()
    if order[0] == "push":
        int_que.append(order[1])
    elif order[0] == "pop":
        if int_que:
            print(int_que.popleft())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(int_que))
    elif order[0] == "empty":
        if int_que:
            print(0)
        else:
            print(1)
    elif order[0] == "front":
        if int_que:
            print(int_que[0])
        else:
            print(-1)
    elif order[0] == "back":
        if int_que:
            print(int_que[-1])
        else:
            print(-1)
