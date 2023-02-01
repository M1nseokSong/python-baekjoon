# 카드2
from collections import deque

n = int(input())
cards = deque()
for _ in range(1, n+1):
    cards.append(_)

while len(cards) != 1:
    cards.popleft()
    tmp = cards.popleft()
    cards.append(tmp)

print(*cards)
