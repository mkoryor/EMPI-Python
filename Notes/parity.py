# The parity of a binary word is 1 if the number of ls in the word is odd; otherwise, it is 0. 
# For example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity checks are used 
# to detect single bit errors in data storage and communication. It is fairly straightforward to write 
#code that computes the parity of a single 64-bit word.

# The brute-force algorithm iteratively tests the value of each bit while tracking the number of ls seen so far. 
# Since we only care if the number of ls is even or odd, we can store the number
# mod 2.


def parity(x):  
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result
    

# Time complexity is O(n), where n is the word size 


def parity(x):
    result = 0
    while x: 
        result ^= 1
        x &= x - 1  # Drops the lowest bit of x.
    return result


# time complexity O(k), where k is the number of bits set to 1 in a particular word.
