w = [3, 4, 2]
v = [4, 5, 3]

total_weight = 7
dp = [[ 0 for _ in range(len(w)+1)] for _ in range(total_weight + 1)]

for i in range(total_weight + 1):
    dp[i][0] = 0

for i in range(1, total_weight + 1):
    for j in range(1, len(w) + 1):
        dp[i][j] = dp[i][j - 1]
        if(w[j-1] <= i):
            dp[i][j] = max( dp[i][j], dp[i - w[j-1]][j] + v[j-1])
for i in dp:
    print(i)
print(dp[-1][-1])