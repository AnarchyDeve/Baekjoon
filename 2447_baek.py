import sys

n = int(sys.stdin.readline())
level = n // 3  # 얼마나 반복해야 할지 결정

# 초기 상태: 별 하나
paper = [['*']]

# 반복해서 확장 (log_3(n)만큼)
while len(paper) < n:
    size = len(paper)
    res = [[' ' for _ in range(size * 3)] for _ in range(size * 3)]

    for i in range(size):
        for j in range(size):
            if paper[i][j] == '*':
                for x in range(3):
                    for y in range(3):
                        if x == 1 and y == 1:
                            continue  # 가운데는 비우기
                        res[i*3 + x][j*3 + y] = '*'

    paper = res  # 다시 기준으로 삼음



# 출력
for row in paper:
    print(''.join(row))

