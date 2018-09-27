

def reverse_bits(x):
    MASK_SIZE = 16
    BIT_MASK = 0XFFFF
    return (PRECOMPUTED_REVERSE[X & BIT_MASK] << (3 * MASK_SIZE) | 
            PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & BIT_MASK] << 
            (2 * MASK_SIZE) | PRECOMPUTED_REVERSE[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE
            | PRECOMPUTED_REVERSE[(x >> (3 * MASK_SIZE)) & BIT_MASK])
            

Time complexity is O(n/L), for n-bit integers and L-bit cache keys.
