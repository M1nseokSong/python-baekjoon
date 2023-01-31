# 동전 0
n, k = map(int, input().split())
# 순서대로 집어 넣고 k보다 작은 동전 중 가장 큰 동전을 뺴 내는 식으로
# 하면 될 듯 => 스택?

# map은 리스트, 튜플 같이 값이 여러개 일 떄 사용.
stack = list(int(input()) for _ in range(n))
count = 0
while k!=0:
    tmp = stack.pop()
    if tmp <= k:
        count += k//tmp
        k = k%tmp

print(count)
