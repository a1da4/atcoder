import math


def main(N):
    ans = []
    for population in range(1, int(math.sqrt(N)) + 1):
        if N % population == 0:
            ans.append(population)
            ans.append(N // population)
            ans = list(set(ans))
    return sorted(ans)


if __name__ == "__main__":
    N = int(input())
    answers = main(N)
    for ans in answers:
        print(ans)
