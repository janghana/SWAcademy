T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    S = input()
    ATK_J, HP_J = map(int, input().split())
    ATK_M, HP_M = map(int, input().split())
    index_monster = {'&': 0}
    index_start = {'@': 0}
    index_end = {'O': []}
    result = False
    cnt = 0
    for i in S:
        if i == 'O':
            index_end['O'].append(cnt)
        elif i == '@':
            index_start['@'] = S.index(i)
        elif i == '&':
            index_monster['&'] = S.index(i)
        cnt += 1
    for i in index_end['O']:
        if index_start['@'] - i > 0:
            if index_monster['&'] > index_start['@']:
                count = 0
                for i in S[i + 1:index_start['@']]:
                    if i == "#":
                        count += 1
                if count <= M:
                    result = True
                    break
            else:
                count = 0
                nTrue = True
                for i in S[i + 1:index_start['@']]:
                    if i == "#":
                        count += 1
                    elif i == "&":
                        while True:
                            HP_M = HP_M - ATK_J
                            if HP_M <= 0:
                                break
                            HP_J = HP_J - ATK_M
                            if HP_J <= 0:
                                nTrue = False
                                break
                if count <= M and nTrue:
                    result = True
                    break
        elif index_start['@'] - i < 0:
            if index_monster['&'] < index_start['@']:
                count = 0
                for i in S[index_start['@'] + 1:i]:
                    if i == "#":
                        count += 1
                if count <= M:
                    result = True
                    break
            else:
                count = 0
                nTrue = True
                for i in S[index_start['@'] + 1:i]:
                    if i == "#":
                        count += 1
                    elif i == "&":
                        while True:
                            HP_M = HP_M - ATK_J
                            if HP_M <= 0:
                                break
                            HP_J = HP_J - ATK_M
                            if HP_J <= 0:
                                nTrue = False
                                break
                if count <= M and nTrue:
                    result = True
                    break
    if result:
        print("HAHA!")
    else:
        print("HELP!")

    # elif S1 != '' and S2 == '':
    #     print(S1, S2)
    #
    #     for i in index_end['O']:
    #         count = 0
    #         nTrue = True
    #         for j in S1[i+1:]:
    #             if j == '#':
    #                 count += 1
    #             elif j == '&':
    #                 while True:
    #                     HP_M -= ATK_J
    #                     if HP_M <= 0:
    #                         break
    #                     HP_J -= ATK_M
    #                     if HP_J <= 0:
    #                         nTrue = False
    #                         break
    #         if count <= M and nTrue:
    #             result = True
    #             break
    # elif S1 != '' and S2 != '':
    #     print(S1, S2)
    #
    #     for i in index_end['O']:
    #         count = 0
    #         nTrue = True
    #         for j in S1[i+1:]:
    #             if j == '#':
    #                 count += 1
    #             elif j == '&':
    #                 while True:
    #                     HP_M -= ATK_J
    #                     if HP_M <= 0:
    #                         break
    #                     HP_J -= ATK_M
    #                     if HP_J <= 0:
    #                         nTrue = False
    #                         break
    #         if count <= M and nTrue:
    #             result = True
    #             break
    #     for i in index_end['O']:
    #         count = 0
    #         nTrue = True
    #         for j in S2[:i]:
    #             if j == '#':
    #                 count += 1
    #             elif j == '&':
    #                 while True:
    #                     HP_M -= ATK_J
    #                     if HP_M <= 0:
    #                         break
    #                     HP_J -= ATK_M
    #                     if HP_J <= 0:
    #                         nTrue = False
    #                         break
    #         if count <= M and nTrue:
    #             result = True
    #             break

    # S1, S2 = map(str, S.split('@'))
    # if S1 == '' and S2 != '':
    #     print(S1, S2)
    #     for i in index_end['O']:
    #         count = 0
    #         nTrue = True
    #         for j in S2[:i]:
    #             print(j)
    #             if j == '#':
    #                 count += 1
    #             elif j == '&':
    #                 while True:
    #                     HP_M -= ATK_J
    #                     if HP_M <= 0:
    #                         break
    #                     HP_J -= ATK_M
    #                     if HP_J <= 0:
    #                         nTrue = False
    #                         break
    #         if count <= M and nTrue:
    #             result = True
    #             break
