if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    """
    :param N: num of items
    :param M: top-k 
    :param A: votes
    if top-k(M) items > 1/4M of sum(A):
      Yes
    else:
      No
    :return: Yes or No
    """
    total = sum(A)
    threshold = total / (4*M)
    count = sum([a>=threshold for a in A])
    if count >= M:
        print('Yes')
    else:
        print('No')

