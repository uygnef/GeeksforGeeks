a = "abcd"
b = "becd"

dp = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]
dp[0][0] = 0

for i, a_chr in enumerate(a):
    i +=1
    for j, b_chr in enumerate(b):
        j += 1
        if a_chr == b_chr:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

for i in dp:
    print(i)
print(dp[-1][-1])