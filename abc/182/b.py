def main(N, A):
    ans = {"num": 0, "GCD-ness": 0}
    for i in range(2, max(A)+1):
        tmp = sum([1 if a%i==0 else 0 for a in A])
        if tmp >= ans["GCD-ness"]:
            ans["num"] = i
            ans["GCD-ness"] = tmp
    return ans

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    ans = main(N, A)
    print(ans["num"])
