T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    S = input()
    result = ''
    for _ in range(M):
        A, B = map(int, input().split())
        tmp = S[A - 1:B]
        nTrue = True
        if len(tmp) > 2:
            if tmp[:3] == 'Umm':
                if tmp[3:] != "m"*len(tmp[3:]):
                    nTrue = False
            else:
                nTrue = False
        else:
            nTrue = False
        if nTrue:
            result += '1'
        else:
            result += '0'
    print(result)
