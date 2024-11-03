
from functools import lru_cache

@lru_cache
def find(N):
    if N == 1:
        return 0
    if N % 2 == 0 and N % 3 == 0:
        return 1 + min(find(N - 1), find(N // 2), find(N // 3))
    elif N % 2 == 0:
        return 1 + min(find(N - 1), find(N // 2))
    elif N % 3 == 0:
        return 1 + min(find(N - 1), find(N // 3))
    else:
        return 1 + find(N - 1)

N = int(input())
print(find(N))
