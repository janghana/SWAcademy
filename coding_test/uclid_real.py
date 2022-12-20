def uc(a, b):
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    else:
        return uc(b % a, a)

def main():
    a, b = map(int, input().split())
    print(uc(a, b))

if __name__ == "__main__":
    main()
