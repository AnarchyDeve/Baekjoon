def eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

# ----------------------- 입력 처리 -----------------------
test = int(input())  # 테스트 케이스 수 입력
nums = []            # 입력된 n값들을 저장할 리스트
max_n = 0            # 입력 중 가장 큰 n을 저장할 변수 (소수 구할 최대 범위 설정)

for _ in range(test):
    n = int(input())    # n 입력
    nums.append(n)      # n 리스트에 저장
    max_n = max(max_n, n)  # 최대 n 갱신 (최적화를 위해)

# ----------------------- 소수 미리 구하기 -----------------------
lst = eratosthenes(max_n)  # 한 번만 소수 구하기

# ----------------------- 각 입력 처리 -----------------------
for n in nums:
    count = 0  # 두 소수 합으로 n이 되는 경우의 수 세기
    
    # 두 포인터 방식으로 합이 n인 두 소수 찾기
    left, right = 0, len(lst) - 1
    while left <= right:
        sum_value = lst[left] + lst[right]
        
        if sum_value == n:
            count += 1
            left += 1
            right -= 1
        elif sum_value < n:
            left += 1
        else:
            right -= 1
    
    print(count)  # 결과 출력
