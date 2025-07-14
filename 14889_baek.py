# 내가 이해를 잘못한 방식

import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())

teams = [list(map(int, input().split())) for _ in range(n)]
res = []

# i < j 인 경우의 팀 능력 합 계산
for i in range(n):
    for j in range(n):
        if i >= j:
            continue
        res.append(teams[i][j] + teams[j][i])

M = Counter(res)

# 중복 합이 존재하면 0 출력
for value, count in M.items():
    if count >= 2:
        print(0)
        break
else:
    # 키(팀 능력 합) 리스트 정렬
    keys = sorted(M.keys())
    min_diff = float('inf')

    # 인접한 값끼리 차이 비교
    for i in range(len(keys) - 1):
        diff = abs(keys[i+1] - keys[i])
        min_diff = min(min_diff, diff)

    print(min_diff)

### combinations 방식
import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]

players = list(range(n))
min_diff = float('inf')

# n명 중 n//2명을 선택해 팀을 구성
for team_a in combinations(players, n // 2):
    team_b = [p for p in players if p not in team_a]

    # 팀 점수 계산 함수
    def team_score(team):
        score = 0
        for i in team:
            for j in team:
                if i != j:
                    score += S[i][j]
        return score

    # 두 팀 점수 차이 계산
    diff = abs(team_score(team_a) - team_score(team_b))
    min_diff = min(min_diff, diff)

print(min_diff)

# DFS 방식
import sys
input = sys.stdin.readline

n = int(input())  # 전체 사람 수 입력
S = [list(map(int, input().split())) for _ in range(n)]  # 능력치 표 입력

visited = [False] * n  # 팀 A에 속한 사람을 표시할 리스트
min_diff = float('inf')  # 점수 차이의 최솟값을 저장할 변수

# DFS로 팀 A를 구성하는 함수
def dfs(depth, idx):
    global min_diff

    # n/2명이 팀 A에 속하게 되면 팀 B는 나머지로 자동 구성됨
    if depth == n // 2:
        team_a, team_b = [], []
        for i in range(n):
            if visited[i]:
                team_a.append(i)  # 팀 A에 포함된 인덱스
            else:
                team_b.append(i)  # 팀 B에 포함된 인덱스

        # 주어진 팀의 점수를 계산하는 함수
        def calc_score(team):
            score = 0
            for i in range(len(team)):
                for j in range(len(team)):
                    if i != j:  # 같은 사람 제외
                        score += S[team[i]][team[j]]
            return score

        # 팀 A, 팀 B 점수 계산
        a_score = calc_score(team_a)
        b_score = calc_score(team_b)

        # 두 팀의 점수 차이의 최소값 갱신
        min_diff = min(min_diff, abs(a_score - b_score))
        return

    # 조합 탐색을 위한 DFS
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True  # i번 사람을 팀 A에 포함
            dfs(depth + 1, i + 1)  # 다음 사람 선택을 위해 재귀 호출
            visited[i] = False  # 백트래킹 (선택 취소)

# DFS 시작: depth=0, idx=0
dfs(0, 0)

# 결과 출력
print(min_diff)
