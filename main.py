def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    
    #Base case
    if n == 0: return 0
    if n == 1: return 1

    #Recursive case
    else:
        return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)

    

def fib_top_down(n, fibs):

    #Case for if this subproblem has already been computer by a previous case
    if fibs[n] != -1:
        return fibs[n]

    #Base case
    if n == 0: fibs[n] = 0
    elif n == 1:fibs[n] = 1

    #Recursive case using DP as discussed in class
    else: 
        fibs[n] = fib_top_down(n - 1, fibs) + fib_top_down(n - 2, fibs)

    return fibs[n]



def fib_bottom_up(n):
    
    #Start by initializing fibs within the function
    fibs = [0] * (n + 1)

    #Base case
    if n >= 1: fibs[1] = 1

    #Iterative case (Equivalent of recursive case but for this new approach)
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]

    return fibs[n]




n = 5
counts = [0] * (n + 1)
fib_number = fib_recursive(n, counts)