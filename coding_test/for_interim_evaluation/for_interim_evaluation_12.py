from collections import Counter
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    S = input()
    index_start = S.index("@")
    index_end = S.index("O")
    index_gauntlet = S.index("G")
    result = False
    tmp_S = S[:]
    if index_start < index_end:
        if abs(index_start - index_gauntlet)-1 <= M:
            result = True
        if index_start < index_gauntlet:
            tmp_S = tmp_S[index_start + 1:index_gauntlet]
        elif index_start > index_gauntlet:
            tmp_S = tmp_S[index_gauntlet + 1:index_start]
        if Counter(tmp_S)['#'] <= M:
            result = True
        S = S[index_start+1:index_end]

    else:
        if abs(index_start - index_gauntlet)-1 <= M:
            result = True
        if index_start < index_gauntlet:
            tmp_S = tmp_S[index_start + 1:index_gauntlet]
        elif index_start > index_gauntlet:
            tmp_S = tmp_S[index_gauntlet + 1:index_start]
        if Counter(tmp_S)['#'] <= M:
            result = True
        S = S[index_end+1:index_start]
    if Counter(S)['#'] <= M:
        result = True

    if result:
        print("HAHA!")
    else:
        print("HELP!")
