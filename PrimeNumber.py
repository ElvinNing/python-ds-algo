N = int(input())
primes = []
if N > 2:
    primes = [2]
    odds = (i for i in range(2, N) if i%2 == 1)
    for m in odds:
        isPrime = True
        for div in range(2, int(m**0.5) + 1):
            if m % div == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(m)

elif N == 2:
	primes = [2]

print(*primes)
