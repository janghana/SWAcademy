result = []
def bracket_check(C_bracket):
    nTrue = "YES"
    bracket_dict = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in C_bracket:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if stack:
                if bracket_dict[char] != stack.pop():
                    nTrue = "NO"
    if stack:
        nTrue = "NO"
    return nTrue
N = int(input())
for _ in range(N):
    C_bracket = input()
    print(bracket_check(C_bracket))
