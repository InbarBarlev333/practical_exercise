def total_sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + total_sum(n // 10)