def main(N):
    ans = None

    alphabets = []
    for i in range(97, 97 + 26):
        alphabets.append(chr(i))

    # 桁数を算出する
    tmp = 0
    for i in range(1, 20):
        if tmp + 26 ** i >= N:
            break
        tmp += 26 ** i
    N -= tmp

    # 各桁でのアルファベットを算出する
    tmp = 0
    ans = []
    # 最も大きい桁から計算
    for j in range(1, i + 1):
        for k in range(26):
            if tmp + 26 ** (i - j) >= N:
                ans.append(k)
                break
            tmp += 26 ** (i - j)

    # 結合
    ans = "".join([alphabets[id] for id in ans])

    return ans


if __name__ == "__main__":
    N = int(input())
    ans = main(N)
    print(ans)
