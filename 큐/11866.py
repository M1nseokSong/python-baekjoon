from collections import deque
n, k = map(int, input().split())
yose = deque()
result = list()
turn = 0
for _ in range(1, n+1):
    yose.append(_)
for _ in range(n):
    if turn+k > len(yose):
        turn = (turn+k-1) % len(yose)
    else:
        turn = turn + k -1  
    result.append(yose[turn])
    yose.remove(yose[turn])

print("<" + ', '.join(map(str, result))+">")


# 1 2 3 4 5 6 7  turn=2
# 1 2 4 5 6 7 // 3 turn =4
# 1 2 4 5 7 // 6 turn=1
# 1 4 5 7 // 2 turn=3
# 1 4 5  // 7 turn =2
# 1 4 // 5 turn = 0
# 4 // 1
#  // 4
