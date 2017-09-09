weights = [2,1, 3, 2]
values = [3,2,4,2]
total = 5
dp = [[None for _ in range(total + 1)] for __ in range(len(weights) + 1)]

def rec(i, remain):
    if i >= len(weights):
        return 0
    if dp[i][remain] != None:
        return dp[i][remain]

    if remain < weights[i]:
        dp[i][remain] = rec(i+1, remain)
        return dp[i][remain]
    else:
        dp[i][remain] = max(rec(i+1, remain), rec(i+1, remain - weights[i]) + values[i])
        return dp[i][remain]

#print(dp)
print(rec(0, 5))
for i in dp:
    print(i)
print(dp)
