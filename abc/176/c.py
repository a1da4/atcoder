
def main(A):
    ans = 0
    max_num = A[0]
    for a in A:
        max_num = max(max_num, a)
        ans += max_num - a

    return ans

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    ans = main(A)
    print(ans)

