class reverse_iter:

    def __init__(self, some_list: list):
        self.some_list = some_list
        self.start = len(some_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.start -= 1
        if self.start >= 0:
            return self.some_list[self.start]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)