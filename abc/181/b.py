if __name__ == "__main__":
    N = int(input())
    ans = 0
    for _ in range(N):
        a, b = map(int, input().split())
        # l = [i for i in range(a, b + 1)]
        # 1 ~ b までの和
        upper = b * (b + 1) / 2
        # 1 ~ (a-1) までの和
        lower = (a - 1) * a / 2
        # ans += sum(l)
        ans += upper - lower

    print(int(ans))
