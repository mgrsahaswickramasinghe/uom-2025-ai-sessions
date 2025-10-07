def Largest_Prime_Factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
print(Largest_Prime_Factor(600851475143))