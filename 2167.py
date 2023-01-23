# 2차원 배열의 합
n, m = map(int, input().split())
array = list(list(map(int, input().split())) for _ in range(n))

memo = [[0] * (m+1) for _ in range(n+1)]

# 메모이제이션 : memo 2차원 배열에 원래 배열 (0, 0) 부터 (a, b)까지의 합을 저장해 놓음.
# memo 2차원 배열은 맨 왼쪽과 위에 0 값이 들어있는 행, 열을 추가하고 시작.
for i in range(1, n+1):
    for j in range(1, m+1):
        memo[i][j] = memo[i][j-1] + memo[i-1][j] - memo[i-1][j-1] + array[i-1][j-1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(memo[x][y] - memo[i-1][y] - memo[x][j-1] + memo[i-1][j-1])
