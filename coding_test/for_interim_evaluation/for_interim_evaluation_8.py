from collections import Counter
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    S = input()
    index_start = S.index("@")
    index_end = S.index("O")
    if index_start < index_end:
        S = S[index_start+1:index_end]
    else:
        S = S[index_end+1:index_start]
    if Counter(S)['#'] > M:
        print("HELP!")
    else:
        print("HAHA!")