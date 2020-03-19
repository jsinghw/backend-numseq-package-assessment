def fib(n):
    '''Write fibonacci series up to n'''
    result = []
    a, b = 0, 1
    if n == 1:
        return(1)
    while len(result) <= n:
        result.append(a)
        a, b = b, a+b
    return result[n]
