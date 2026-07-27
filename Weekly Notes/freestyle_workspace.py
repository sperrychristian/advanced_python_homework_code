
def fibrec(n):
    if n < 2:
        return n
        
    return fibrec(n - 1) + fibrec(n - 2)
    
print(fibrec(100))