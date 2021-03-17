"""

"""

def superDigit(n, k):
    
    res = recursiveHelper(n)
    mult = res * k
    
    return recursiveHelper(str(mult))
    

    
    
def recursiveHelper(n:str) -> int:
        
    if len(n)==1:
        return int(n)
        
    total = sum([int(digit) for digit in n])
        
    return recursiveHelper(str(total))
    