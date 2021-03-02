def main():
    for n in range(226):
        print(n)
        if isPowerOfTwo(n):
            print('iterative: Yes')
        else:
            print('iterative: No')
        if isPowerOf2(n):
            print('recursive: Yes')
        else:
            print('recursive: No')
        print('------------------')


def isPowerOfTwo(n):
    if n == 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True


def isPowerOf2(n):
    if n == 1:
        return True
    elif n % 2 != 0 or n == 0:
        return False
    return isPowerOf2(n / 2)


if __name__ == '__main__':
    main()
