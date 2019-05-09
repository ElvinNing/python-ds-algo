'''Naive Recursion'''
def fib_recursion(n):
    if n <= 1: # Base
        return n
    return fib_recursion(n-1) + fib_recursion(n-2) # Recursion

print(fib_recursion(5))

# fib(5)
# fib(4) + fib(3)
# (fib(3) + fib(2)) + (fib(2) + fib(1))
# ((fib(2) + fib(1)) + (fib(1) + fib(0))) + ((fib(1) + fib(0)) + fib(1))
# (((fib(1) + fib(0)) + fib(1)) + (fib(1) + fib(0))) + ((fib(1) + fib(0)) + fib(1))

'''Top Down Memoization'''
memo = {0: 0, 1: 1} # memo[0] = 0, memo[1] = 1
def fib_memo(n):
    if n in memo.keys():
        return memo[n]
    return fib_memo(n-1) + fib_memo(n-2)

print(fib_memo(5))

'''Bottom Up Iteration'''
def fib_iteration(n):
    if n <= 1:
        return n
    else:
        previous, current = 0, 1
        while n > 1:
            previous, current = current, previous + current
            n -= 1
    return current
    
print(fib_iteration(5))
