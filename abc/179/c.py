from math import sqrt

def main(N):
    # i*i<N を満たす数
    ans = -int(sqrt(N)//1) if int(sqrt(N)//1)**2 != N else -int(sqrt(N)//1)+1
    tmp = 0
    # i*j<N (j>i) を満たす数
    for i in range(1, int(sqrt(N)//1)+1):
        print(f'{i}: {int(N//i)}') if N%i != 0 else print(f'{i}: {int(N//i)-1}')
        tmp += int(N//i)
        tmp -= i-1
        if N%i == 0:
            tmp -= 1
    ans += tmp*2

    return ans

if __name__ == '__main__':
    N = int(input())
    ans = main(N)
    print(ans)

