def number_factor(n, mem):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n == 3:
        return 2
    elif n not in mem:
        mem[n] = number_factor(n - 4, mem) + number_factor(n - 3, mem) + number_factor(n - 1, mem)
    return mem[n]


print(number_factor(7, {}))
