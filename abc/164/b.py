"""
:param A: HP takahashi
:param B: Attack takahashi
:param C: HP aoki
:param D: Attack aoki
:return: takahashi win or lose
"""
A, B, C, D = map(int, input().split())
tk_count = C//B if C%B==0 else C//B + 1
ao_count = A//D if A%D==0 else A//D + 1
print(tk_count, ao_count)
if tk_count <= ao_count:
    print('Yes')
else:
    print('No')


