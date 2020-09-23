import time

def main(S, T):
    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += 1
    return ans

if __name__ == '__main__':
    start = time.time()
    S = input()
    T = input()
    ans = main(S, T)
    print(ans)
    print(f'{time.time() - start}sec')

