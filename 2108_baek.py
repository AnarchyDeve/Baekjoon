import sys
import statistics

# 입력 받기
N = int(sys.stdin.readline().strip())
numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]

# 산술평균 (반올림하여 소수점 이하 첫째 자리까지 출력)
mean = round(statistics.mean(numbers))

# 중앙값
median = statistics.median(numbers)

# 최빈값 구하기
freq = statistics.multimode(numbers)
freq.sort()  # 여러 개일 경우 오름차순 정렬
mode = freq[1] if len(freq) > 1 else freq[0]  # 두 번째로 작은 값 선택

# 범위
range_value = max(numbers) - min(numbers)

# 출력
print(mean)
print(median)
print(mode)
print(range_value)