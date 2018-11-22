

def delete_duplicate(A):
    
    if not A:
        return []
        
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] = A[i]:
            A[write_index] = A[i]
            write_index += 1
    
     return write_index 
     
     
# The time complexity is 0(n), and the space complexity is 0(1), since all that is needed is the two additional variables.












