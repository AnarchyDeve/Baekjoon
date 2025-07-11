import sys

# 전역 변수 선언
count = 0        # 저장(assign) 횟수를 셈
answer = -1      # K번째 저장 값 (기본값은 -1)

# 병합 정렬 함수
def merge_sort(arr, left, right, k):
    global count, answer
    if left < right:
        mid = (left + right) // 2

        # 왼쪽 절반 정렬
        merge_sort(arr, left, mid, k)

        # 오른쪽 절반 정렬
        merge_sort(arr, mid + 1, right, k)

        # 정렬된 두 절반을 병합
        merge(arr, left, mid, right, k)

# 병합(merge) 함수
def merge(arr, left, mid, right, k):
    global count, answer

    i = left         # 왼쪽 배열 포인터
    j = mid + 1      # 오른쪽 배열 포인터
    temp = []        # 임시 리스트

    # 두 포인터 비교하며 정렬된 값 저장
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    # 왼쪽 배열에 남은 요소 추가
    while i <= mid:
        temp.append(arr[i])
        i += 1

    # 오른쪽 배열에 남은 요소 추가
    while j <= right:
        temp.append(arr[j])
        j += 1

    # 정렬된 temp 배열을 원래 arr에 복사 (이 때 저장 횟수 증가!)
    for t in range(len(temp)):
        arr[left + t] = temp[t]
        count += 1  # 저장(assign) 1회 발생

        # K번째 저장이면 answer 저장
        if count == k:
            answer = temp[t]

# 입력 처리
n, k = map(int, input().split())         # 배열 크기 N, 찾을 저장 번호 K
arr = list(map(int, input().split()))    # 배열 입력

merge_sort(arr, 0, n - 1, k)             # 병합 정렬 시작
print(answer)                            # 결과 출력
