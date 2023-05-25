# 너무 완벽하게 모든 조건을 담아서 풀려고 한듯,,
# 가끔은 브루트포스를 떠올리자,,
# 시간 복잡도는 O(nm) 이여서 시간초과가 안나는듯 하다..

import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
answer = abs(100-n)
if m: 
    broken = list(input().split())
else:
    broken = list()

# 작은수에서 큰수로 이동할땐 500,000 까지만 보면 되지만
# 반대로 큰수에서 작은수로 내려올수도 있으므로 1,000,000 까지 봐야함
for num in range(1000001): 
    for N in str(num):
        if N in broken: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
            break
    else: # 번호를 눌러서 만들 수 있는 경우엔
    	# min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
        answer = min(answer, len(str(num)) + abs(num - n))

print(answer)
