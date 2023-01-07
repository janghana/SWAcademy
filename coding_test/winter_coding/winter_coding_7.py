from itertools import combinations
S, N = map(str,input().split())
S_com = list(combinations(S,int(N)))
tmp_S = S[:]
nTrue = False
for i in S_com:
    for j in i:
        S = list(S)
        S.remove(j)
    if len(S) % 2 == 0:
        check = 0
        for i in range(len(S)//2):
            if S[i] == S[len(S) - i - 1]:
                check += 1
        if check == len(S)//2:
            nTrue = True
    else:
        check = 0
        for i in range(len(S)//2):
            if S[i] == S[len(S) - i -1]:
                check += 1
        if check == len(S)//2:
            nTrue = True
    S = tmp_S[:]
print(nTrue)
