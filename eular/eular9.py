def Special_Pythagorean_Triplet():
    for a in range(1, 1000):
        for b in range(a, 1000 - a):
            c = 1000 - a - b
            if a * a + b * b == c * c:
                return a * b * c
print(Special_Pythagorean_Triplet())