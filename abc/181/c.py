from itertools import combinations


def is_inline(z1, z2, z3):
    if z1[0] == z2[0] == z3[0] or z1[1] == z2[1] == z3[1]:
        return True
    if (
        z1[0] == z2[0]
        or z2[0] == z3[0]
        or z3[0] == z1[0]
        or z1[1] == z2[1]
        or z2[1] == z3[1]
        or z3[1] == z1[1]
    ):
        return False
    if (z1[1] - z2[1]) / (z1[0] - z2[0]) == (z3[1] - z2[1]) / (z3[0] - z2[0]):
        return True
    return False


def main(Z):
    for z1, z2, z3 in combinations(Z, 3):
        # 直線上にあるか判断
        if is_inline(z1, z2, z3):
            print(z1, z2, z3)
            return "Yes"
    return "No"


if __name__ == "__main__":
    N = int(input())
    Z = []
    for _ in range(N):
        x, y = map(int, input().split())
        Z.append([x, y])
    ans = main(Z)
    print(ans)
