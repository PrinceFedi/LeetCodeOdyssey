def fib(n, mem):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n not in mem:
        mem[n] = fib(n-1, mem) + fib(n-2, mem)
    return mem[n]


print(fib(5, {}))
