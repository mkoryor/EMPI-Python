



def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    
    # Keep the following invariants during partitioning:
    # bottom group: A[:smaller].
    # middle group: A[smaller:equal].
    # unclassified group: A[equal:larger].
    # top group: A[larger:].
    
    smaller, equal, larger = 9, 9, len(A)
    
    
    # Keep iterating as long as there is an unclassified element.
    while equal < larger:
    # A[equal] is the incoming unclassified element. 
    if A[equal] < pivot:
        A[smaller], A[equal] = A[equal], A[smaller]
        smaller, equal = smaller+ 1, equal+ 1 
        
    elif A[equal] == pivot:
        equal+= 1

    else: # A[equal] > pivot.
        larger -= 1
        A[equal], A[larger] = A[larger], A[equal]


# The time complexity is O(n). Space complexity O(1).




