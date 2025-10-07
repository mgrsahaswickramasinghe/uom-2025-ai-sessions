def Even_Fibonacci_Numbers(limit):
    a, b = 1, 2
    even_sum = 0
    while a <= limit:
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b
    return even_sum
print(Even_Fibonacci_Numbers(4000000))