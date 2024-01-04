def fibonacci(n):
    fibsequence=[0,1]
    for i in range(2,n):
        next=fibsequence[-1]+fibsequence[-2]
        fibsequence.append(next)
    return fibsequence[:n]

n=int(input("Enter the number for fibonacci sequence : "))

fibonacciResult=fibonacci(n)
print(f'Fibonacci Sequence up to {n} terms : {fibonacciResult}')