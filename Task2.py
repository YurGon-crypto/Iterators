def in_range(*args):
    num_args = len(args)
    
    if num_args == 0 or num_args > 3:
        raise TypeError("in_range expected at least 1 argument, got 0")
    elif num_args == 1:
        stop = args[0]
        start, step = 0, 1
    elif num_args == 2:
        start, stop = args
        step = 1
    elif num_args == 3:
        start, stop, step = args

   
    if step == 0:
        raise ValueError("in_range() arg 3 must not be zero")

  
    num_elements = max(0, (stop - start + step - (1 if step > 0 else -1)) // step)

  
    result = []
    current = start
    for _ in range(num_elements):
        result.append(current)
        current += step

    return result


print(in_range(5))            # [0, 1, 2, 3, 4]
print(in_range(2, 10))         # [2, 3, 4, 5, 6, 7, 8, 9]
print(in_range(2, 10, 2))      # [2, 4, 6, 8]
print(in_range(10, 2, -2))     # [10, 8, 6, 4]
