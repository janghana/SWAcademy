from collections import Counter

char_val = input()

if Counter(char_val)['('] == Counter(char_val)[')']:
    print("YES")
else:
    print("NO")



