## override the statistics. median function to compute the moving of a list of numbers  
def moving_median(numbers, window_size):
    if window_size <= 0:
        raise ValueError("Window size must be positive")
    if not numbers:
        return []

    medians = []
    for i in range(len(numbers)):
        start_index = max(0, i - window_size + 1)
        window = numbers[start_index:i + 1]
        sorted_window = sorted(window)
        n = len(sorted_window)
        mid = n // 2
        if n % 2 == 0:
            median = (sorted_window[mid - 1] + sorted_window[mid]) / 2
        else:
            median = sorted_window[mid]
        medians.append(median)
    
    return medians

print(moving_median([1, 3, 5, 7, 9], 3))  # Example usage
print(moving_median([10, 20, 30, 40, 50], 2))  # Example usage
print(moving_median([5, 15, 25, 35, 45], 4))  # Example usage
print(moving_median([], 3))  # Edge case: empty list    