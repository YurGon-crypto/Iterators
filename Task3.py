class MyIterable:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += self.step
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        if 0 <= index < len(self):
            return self.start + index * self.step
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        return max(0, (self.end - self.start + self.step - 1) // self.step)


my_iterable = MyIterable(1, 10, 2)
for num in my_iterable:
    print(num)

print(my_iterable[2])  

