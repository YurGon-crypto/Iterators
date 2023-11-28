def in_range(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step


for num in in_range(1, 10, 2):
    print(num)
