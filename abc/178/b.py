def main(a, b, c, d):
    ans = -float('inf')
    for x in range(a, b+1):
        for y in range(c, d+1):
            z = x * y
            if ans < z:
                ans = z
    return ans

def main2(a, b, c, d):
    ans = -float('inf')
    for x in [a, b]:
        for y in [c, d]:
            z = x * y
            if ans < z:
                ans = z
    return ans

if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    #ans = main(a, b, c, d)
    ans = main2(a, b, c, d)
    print(ans)

