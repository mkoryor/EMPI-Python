import random

def random_sampling(k, A):
    for i in range(k):
		    r = random.randint(i, len(A) - 1)
	  A[i], A[r] = A[r], A[i]
    
    
# The algorithm runs in additional 0(1) space. The time complexity is O(k) to select the elements.










