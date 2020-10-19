from math import pi, cos, sqrt


def main(A, B, H, M):
    ACB = abs((H + M / 60) / 12 - M / 60) * 2 * pi
    ans = sqrt(A ** 2 + B ** 2 - 2 * A * B * cos(ACB))
    return ans


if __name__ == "__main__":
    A, B, H, M = map(int, input().split())
    ans = main(A, B, H, M)
    print(ans)
