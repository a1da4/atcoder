def main(S):
    ans = S
    if S[-1] == 's':
        return ans + 'es'
    else:
        return ans + 's'

if __name__ == '__main__':
    S = input()
    ans = main(S)
    print(ans)

