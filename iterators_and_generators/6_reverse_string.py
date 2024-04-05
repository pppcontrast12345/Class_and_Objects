def reverse_text(string):
    for char in reversed(string):
        yield char


for char in reverse_text("step"):
    print(char, end='')


def reverse_text(string):
    for char in string[::-1]:
        yield char


for char in reverse_text("step"):
    print(char, end='')


def reverse_text(string):
    idx = 0
    start_idx = len(string) - 1
    while idx < len(string):
        curr_char = string[start_idx - idx]
        yield curr_char
        idx += 1

for char in reverse_text("step"):
    print(char, end='')