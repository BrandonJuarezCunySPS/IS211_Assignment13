# recursion.py

# Part I: Fibonacci Sequence Implementation (Recursive)
def fibonacci(n):
    # Base case: return 0 for F(0) and 1 for F(1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)


# Part II: Euclid’s GCD Algorithm (Recursive)
def gcd(a, b):
    # Base case: if b is 0, gcd(a, 0) = a
    if b == 0:
        return a
    else:
        # Recursive case: gcd(a, b) = gcd(b, a % b)
        return gcd(b, a % b)


# Part III: String Comparison (Recursive)
def compareTo(s1, s2):
    # Base case: if both strings are empty, they are equal
    if len(s1) == 0 and len(s2) == 0:
        return 0
    elif len(s1) == 0:
        return -1  # s1 is empty, so s1 < s2
    elif len(s2) == 0:
        return 1   # s2 is empty, so s1 > s2
    else:
        # Compare the first character of each string
        if s1[0] < s2[0]:
            return -1
        elif s1[0] > s2[0]:
            return 1
        else:
            # If the first characters are the same, compare the rest of the strings
            return compareTo(s1[1:], s2[1:])


#Test the functions
if __name__ == "__main__":
    # Test the fibonacci function
    print("Fibonacci(10):", fibonacci(10))  # Expected Output: 55

    # Test the gcd function
    print("GCD(48, 18):", gcd(48, 18))  # Expected Output: 6

    # Test the compareTo function
    print("Compare 'apple' to 'banana':", compareTo("apple", "banana"))
    print("Compare 'grape' to 'grape':", compareTo("grape", "grape"))
    print("Compare 'water' to 'tea':", compareTo("water", "tea"))
