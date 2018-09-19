# Malfred Koryor


# The Following Program tests bits one-at-a-time starting with the least significant bit

def count_bits(x):
    num_bits = 0
    
    while x:
        num_bits += x & 1
        x >> 1
    return num_bits
    
#Complexity O(n) where n is the number of bits needed to represent the integer
