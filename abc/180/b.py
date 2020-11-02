import math


def manhattan(X):
    m = sum([abs(x) for x in X])
    return m


def euclidean(X):
    e = sum([abs(x) ** 2 for x in X])
    e = math.sqrt(e)
    return e


def chebyshev(X):
    c = max([abs(x) for x in X])
    return c


if __name__ == "__main__":
    N = int(input())
    X = list(map(int, input().split()))
    m = manhattan(X)
    print(m)
    e = euclidean(X)
    print(e)
    c = chebyshev(X)
    print(c)
