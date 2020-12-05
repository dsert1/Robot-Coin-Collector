def collector(coins, mags, n):
    """
    Finds a path that maximizes points
    Args:
        coins (List[List[int]]): 1 at coins[i][j] if there's a coin at (i,j), else 0
        mags (List[List[int]]): 1 at mags[i][j] if there's a magnifier at (i,j), else 0
        n (int): dimensions of the nxn board
    """
    parent = {}
    memo = {}

    def DP(i, j, m):
        '''i: the current col (horiz)
        j: the current row (vert)
        m: number of multipliers in our "backpack"
        '''
        if (i, j, m) in memo:
            return memo[(i, j, m)]




        # BASE CASES
        if i == n-1 and j == n-1:
            return 0



                # coins[n-1][n-1]*m

        # RECURSE


        a, b = -float('inf'), -float('inf')
        if i + 1 < n:
            a = DP(i+1, j, 0) + coins[i][j]*2**m
        # print('\n')
        # print('i, j: ', (i, j))
        # print('coin@i, j?: ', coins[i][j])
        # print('a: ', a)
        # print('\n')
        if j + 1 < n:
            b = DP(i, j+1, m + mags[i][j]) + coins[i][j]*2**m
        # print('****B****\n')
        # print('i, j: ', (i, j))
        # print('coin@i, j?: ', coins[i][j])
        # print('b: ', b)
        # print('\n')

        memo[(i, j, m)] = max(a, b)
        # track which one was max, then make those params the parent param
        # mapped to the prev subprob e.g(i, j+1, 0), etc

        # figure out if it was a or b that was the max
        if memo[(i, j, m)] == a:
            max_was = a
        else:
            max_was = b

        # make the parent map to the max of a, b's params
        if max_was == a:
            # parent[(i, j, m)] = i, j+1, 0
            parent[(i, j, m)] = i+1, j, 0
        else:
            # parent[(i, j, m)] = i+1, j, m + mags[i][j]
            parent[(i, j, m)] = i, j+1, m + mags[i][j]


        return memo[(i, j, m)] # optimal score you can get form this pos




    points = DP(0, 0, 0)
    print('max_points: ', points)

    # go thru parent pointers to get the path

    out = []
    current = (0, 0, 0)
    print('parent dict: ', parent)
    while True:
        out.append((current[0], current[1]))
        if current not in parent:
            break
        print('current: ', current)
        print('parent[current]: ', parent[current])
        current = parent[current]
    # out.append((n-1, n-1))
    return out

if __name__ == '__main__':
    coins, mag, n, points = [[0, 0, 1], [1, 1, 1], [0, 0, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 3, 4
    res = collector(coins, mag, n)

    print('exp: ', points)
    print('\ngot: \n', res)
