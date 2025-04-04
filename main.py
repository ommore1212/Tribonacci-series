def tribonacci_series(n):
    trib = [0, 1, 1]
    while len(trib) < n:
        trib.append(trib[-1] + trib[-2] + trib[-3])
    return trib[:n]

# Example usage
n = int(input("Enter the number of terms: "))
print("Tribonacci Series:")
print(tribonacci_series(n))
