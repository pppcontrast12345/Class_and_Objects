class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.iterations += 1
        if self.iterations >= self.count:
            raise StopIteration

        return self.iterations * self.step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)