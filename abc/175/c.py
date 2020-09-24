def main(X, K, D):
    ans = 0
    X = abs(X)
    # 0に近づける回数を獲得
    time = round(X//D)
    if time > K:
        time = K
    if time == 0:
        # Xとabs(X-D)のどちらがより0に近いのか
        if X <= abs(X-D):
            time = 0
        else:
            time = 1
    # それ以外の回数は単に往復する
    ans = X-time*D
    if (K-time)%2 != 0:
        ans = abs(ans) - D
    return abs(ans)

if __name__ == '__main__':
    X, K, D = map(int, input().split())
    ans = main(X, K, D)
    print(ans)

