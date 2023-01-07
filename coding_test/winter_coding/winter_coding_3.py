S, N = map(str, input().split())

result = []
if S == 'Stack':
    for i in range(int(N)):
        s = input()
        if len(s) == 1:
            if s == '0':
                print(len(result))
            elif s == '1':
                print(result[-1])
            elif s == '2':
                result.pop()
        else:
            result.append(s[2:])
else:
    for i in range(int(N)):
        s = input()
        if len(s) == 1:
            if s == '0':
                print(len(result))
            elif s == '1':
                print(result[0])
            elif s == '2':
                result.remove(result[0])
        else:
            result.append(s[2:])
