def sum_of_the_multiples_of_3_and_5_below(n):
    """
    Find the sum of all the multiples of 3 or 5 below n.

    Args:
    n (int): The upper limit (exclusive).

    Returns:
    int: The sum of all multiples of 3 or 5 below n.
    """
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0) 

print(sum_of_the_multiples_of_3_and_5_below(1000))