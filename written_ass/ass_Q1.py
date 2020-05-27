def Intersect(A,B):
    if A is equal to [] OR B is equal to []:
        return []
    else if A.Len is equal to 1 and B.Len is equal to 1:
        if A is equal to B:
            return A
        else:
            return []
    else:
        A_left = A[:A.Len/2]
        A_right = A[A.Len/2:]
        B_left = B[:B.Len/2]
        B_right = B[B.Len/2:]
        result = Intersect(A_left,B_left)+Intersect(A_right,B_left)
                +Intersect(A_left,B_right)+Intersect(A_right,B_right)
        return result

def divideToSublist(A,B,k):
    if k<2:
        return [A],[B]
    else:    
        A_left = A[:A.Len/2]
        A_right = A[A.Len/2:]
        B_left = B[:B.Len/2]
        B_right = B[B.Len/2:]
        A1,B1 = divideToSublist(A_left,B_left,floor(k/2))
        A2,B2 = divideToSublist(A_right,B_right,k-floor(k/2))
        return A1+A2,B1+B2
    
