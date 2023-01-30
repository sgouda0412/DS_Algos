def uniquePaths(m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]
            print(dp[i][j])
    return dp[m-1][n-1]

##    dp = [1] * n
##    for i in range(1, m):
##        for j in range(1, n):
##            dp[j] += dp[j-1]
##    return dp[-1]
##    dp = [[0 for _ in range(n)] for _ in range(m)]
##    for i in range(m):
##        dp[i][0] = 1
##    for j in range(n):
##        dp[0][j] = 1
##    for i in range(1, m):
##        for j in range(1, n):
##            dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]
##    return dp[m-1][n-1]


if __name__ == "__main__":
    m = 3
    n = 7
    print(uniquePaths(m, n))

x = [[1 for _ in range(4)] for _ in range(3)]
x = [[1 for _ in range(3)] for _ in range(4)]
print(x)

for i in range(3):
    for j in range(4):
        print([i, j])
    if [1, 2] == False:
        break
