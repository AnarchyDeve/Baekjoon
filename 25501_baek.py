n = int(input())

for _ in range(n):
    sen = input()
    rev_sen = sen[::-1]

    if sen == rev_sen:
        print(1, len(sen)//2+1)
    else:
        count = 0
        for i, j in zip(sen, rev_sen):
            if i != j:
                print(0, count+1)
                break

            count += 1