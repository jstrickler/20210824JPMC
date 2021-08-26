LIMIT = 1000000

flags = [True] * (LIMIT + 1)

for n in range(2, (LIMIT + 1)):
    if flags[n]:  # n is prime
        print(n, end=' ')
        for j in range(n * 2, LIMIT + 1, n):
            flags[j] = False
