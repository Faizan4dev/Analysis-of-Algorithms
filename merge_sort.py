def merge(A, p, q, r):
    # copy left and right halves
    L = A[p:q+1]       # A[p..q]
    R = A[q+1:r+1]     # A[q+1..r]
    
    # sentinel values
    L.append(float('inf'))
    R.append(float('inf'))
    
    i = 0   # L pointer
    j = 0   # R pointer
    
    for k in range(p, r+1):        # k = p to r
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:                      # more than one element
        q = (p + r) // 2           # midpoint
        merge_sort(A, p, q)        # sort left half
        merge_sort(A, q+1, r)      # sort right half
        merge(A, p, q, r)          # merge both halves


A = [38, 27, 43, 3, 9, 82, 10]
merge_sort(A, 0, len(A)-1)
print(A)
# [3, 9, 10, 27, 38, 43, 82]