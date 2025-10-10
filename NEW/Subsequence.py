## x0="apple", y0="asfsppsdsdle" --> True if all characters of x0 are in y0 in oder , y0="bsdpple"---> false, y0="paple" --> false
def is_subsequence(x0, y0):
    it = iter(y0)
    return all(char in it for char in x0)   
print(is_subsequence("apple", "asfsppsdsdle"))  # True
print(is_subsequence("apple", "bsdpple"))       # False 
print(is_subsequence("apple", "paple"))        # False