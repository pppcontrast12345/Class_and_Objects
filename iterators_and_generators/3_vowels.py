# class vowels:
#
#     def __init__(self, string: str):
#         self.string = string
#         self.vowels = ["a", "e", "i", "u", "y", "o"]
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.index < len(self.string):
#             current_char = self.string[self.index]
#             self.index += 1
#             if current_char.lower() in self.vowels:
#                 return current_char
#         raise StopIteration
#
#
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)
#

class vowels:

    def __init__(self, string: str):
        self.string = string
        self.vowels = ["a", "e", "i", "u", "y", "o"]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):    # 0            # 12
        for idx in range(self.index, len(self.string)):
            curr_char = self.string[idx]  # += 1 for every iteration

            if curr_char.lower() in self.vowels:
                self.index = idx + 1
                return curr_char
        raise StopIteration


my_string = vowels('Abcedifuty0o')  # 12 chars
for char in my_string:
    print(char)