n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white_paper = [[0] * 100 for i in range(100)]
# 아래와 같이 2차원 배열 선언하면 안됨!!
# white_paper = [[0]*100]*100
result = 0 

for _ in range(n):
    for row in range(paper[_][1], paper[_][1]+10):
        for col in range(paper[_][0], paper[_][0]+10):
            white_paper[row][col] = 1

for _ in white_paper:
    result += sum(_)
print(result)
