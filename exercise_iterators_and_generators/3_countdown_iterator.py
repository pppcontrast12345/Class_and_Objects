class countdown_iterator:

    def __init__(self, count: int):
        self.count = count
        self.reducer = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.reducer >= self.count:
            raise StopIteration

        self.reducer += 1
        result = self.count - self.reducer

        return result



iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")