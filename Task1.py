def with_index(iterable, start=0):
    for i, element in enumerate(iterable, start=start):
        yield i, element


my_list = ['apple', 'banana', 'orange']
for index, value in with_index(my_list, start=1):
    print(f"Index: {index}, Value: {value}")