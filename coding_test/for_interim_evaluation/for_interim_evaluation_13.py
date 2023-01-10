T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    A, B = map(int, input().split())
    S = S[A - 1:B]
    result = True
    if len(S) > 2:
        if S[0:3] == 'Umm':
            for i in S[3:]:
                if i != 'm':
                    result = False
        else:
            result = False
    else:
        result = False

    if result:
        print("YES")
    else:
        print("NO")
