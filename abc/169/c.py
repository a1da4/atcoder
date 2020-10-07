def main(A, B):
    B = round(100 * B)
    ans = A * B
    return int(ans // 100)


if __name__ == "__main__":
    A, B = input().split()
    A = int(A)
    B = float(B)
    ans = main(A, B)
    print(ans)
