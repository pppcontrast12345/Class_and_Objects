# def genrange(start: int, end: int) -> list:
#
#     for num in range(start, end + 1):
#         yield num
#
#
# print(list(genrange(1, 10)))



def genrange(start: int, end: int) -> list:
    while start <= end:
        yield start
        start += 1


print(list(genrange(1, 10)))