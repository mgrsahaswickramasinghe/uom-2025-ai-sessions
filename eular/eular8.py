def Largest_Product_in_a_Series(n, series):
    max_product = 0
    for i in range(len(series) - n + 1):
        product = 1
        for j in range(n):
            product *= int(series[i + j])
        if product > max_product:
            max_product = product
    return max_product
print(Largest_Product_in_a_Series(13,
"73167176531330624919225119674426574742355349194934"))