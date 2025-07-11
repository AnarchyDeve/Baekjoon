import sys

# 메모이제이션을 위한 딕셔너리
dic = {0: 0, 1: 1}

# 피보나치 함수 (메모이제이션 적용)
def fib(n):
    if n in dic:  # 이미 계산된 값이면 바로 반환
        return dic[n]
    
    # 값이 없으면 재귀적으로 계산하여 저장
    dic[n] = fib(n - 1) + fib(n - 2)
    return dic[n]

# 입력 받기
n = int(sys.stdin.readline().strip())

# 피보나치 계산 및 출력
print(fib(n))