from time import time

if __name__ == '__main__':
    s = time()
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i%3 > 0 and i%5 > 0:
            ans += i
    e = time() - s
    print(ans)
    print(f'{e}sec')

