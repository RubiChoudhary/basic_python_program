MOD = 10**9 + 7

# Input
T = int(input())
for _ in range(T):
    A, B, C, N = map(int, input().split())
    
    geek_series = [A, B, C]

    for i in range(3, N):
        next_term = (geek_series[i-1] + geek_series[i-2] + geek_series[i-3]) % MOD
        geek_series.append(next_term)

    result = geek_series[N-1]
    print(result)
# Input:
# 3
# 1 3 2 4
# 1 3 2 5
# 1 3 2 6

# Output:
# 6
# 11
# 19
