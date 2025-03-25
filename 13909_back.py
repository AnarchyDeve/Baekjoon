### 제곱수들은 소수이기 때문에 소수와 제곱수만 갯수 구하기
n = int(input())

for i in lst:
    if i**2 <= n:
        count += 1
print(count)



###실패 코드 열고 닫고를 하나씩 한것

# n = int(input())  # 입력받은 n
# lst = [1] * (n + 1)  # 0부터 n까지 (배열 크기를 n+1로, 인덱스가 1부터 n까지 사용)

# # 1은 의미가 없으므로 초기화
# lst[0] = lst[1] = 0  # 1은 제외

# # 배수마다 열고 닫는 작업
# for i in range(2, n + 1):
#     for j in range(i, n + 1, i):  # i의 배수들에 대해
#         if lst[j] == 1:  # 열려있으면 닫고
#             lst[j] = 0
#         else:  # 닫혀있으면 열고
#             lst[j] = 1

# # 출력: 열린 상태인 값들의 합 (소수 개수)
# print(sum(lst))
