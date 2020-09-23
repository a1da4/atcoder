def main(N):
    max_chain = 0
    chain = 0
    for _ in range(N):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            chain += 1
        else:
            if chain > max_chain:
                max_chain = chain
            chain = 0
    if chain > max_chain:
        max_chain = chain
    chain = 0
    if max_chain >= 3:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    N = int(input())
    ans = main(N)
    print(ans)

