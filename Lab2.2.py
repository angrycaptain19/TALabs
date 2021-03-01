# import sys

# sys.setrecursionlimit(3000)

def main():
    for n in range(2, 11):  # min value > 1 so 0<m<n according to following line
        for m in range(1, n):  # min value >0, max value <n
            print(f'For m={m} and n={n}')
            print(int(binomial(m, n)))
            print(int(binomial(m, n - 1)) + int(binomial(m - 1, n - 1)))


def binomial(m, n):
    if m > n:
        return 0
    elif m == 0 or m == n:
        return 1
    else:
        # bi = factorial(n) // (factorial(m) * factorial(n - m))
        return binomial(m, n - 1) + binomial(m - 1, n - 1) # bi



def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


"""
def factorial(m):
    prod = 1
    for n in range(2, m + 1):
        prod = prod * n
    return prod
"""

if __name__ == '__main__':
    main()
