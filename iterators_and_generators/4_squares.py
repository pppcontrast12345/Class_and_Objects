# def squares(n):
#     for num in range(n):
#         num += 1
#         if num <= n:
#             yield num ** 2
#
#
# print(list(squares(5)))


# def squares(n):
#     for num in range(1, n + 1):
#         yield num ** 2
#
#
# print(list(squares(5)))


def squares(n):
    first_num = 0
    while first_num < n:
        first_num += 1
        yield first_num ** 2


print(list(squares(5)))