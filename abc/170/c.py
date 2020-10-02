def main(X, N, P):
    ans = None
    min_dis = 1e8
    # 0~101 の範囲で考える(1、100が与えられる場合がある為)
    for i in range(102):
        # print(f"loop {i}")
        if i in P:
            continue
        # print(abs(X - i))
        if abs(X - i) < min_dis:
            ans = i
            min_dis = abs(X - i)
            # print(ans)

    return ans


if __name__ == "__main__":
    X, N = map(int, input().split())
    P = list(map(int, input().split()))
    ans = main(X, N, P)
    print(ans)
