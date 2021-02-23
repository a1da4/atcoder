def main(A, B):
    """ calculate num of follow
    :return: number of follow
    """
    return (2 * A + 100) - B

if __name__ == '__main__':
    A, B = map(int, input().split())
    ans = main(A, B)
    print(ans)
    
