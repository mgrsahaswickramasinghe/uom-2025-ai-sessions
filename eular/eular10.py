def Summatio_of_Primes(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return sum(i for i, prime in enumerate(sieve) if prime)
print(Summatio_of_Primes(2000000))