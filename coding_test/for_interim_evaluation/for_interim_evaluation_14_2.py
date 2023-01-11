T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    S = input()
    result = 0
    for _ in range(M):
        A, B = map(int, input().split())
        nTrue = True

        if B - A + 1 <= 2:
            nTrue = False
        elif B - A + 1 > 2:
            if S[A - 1] != 'U':
                nTrue = False
            elif S[A:B] != "m" * (B - A):
                nTrue = False
        if nTrue:
            result += 1
        else:
            result += 0

    print(result)
