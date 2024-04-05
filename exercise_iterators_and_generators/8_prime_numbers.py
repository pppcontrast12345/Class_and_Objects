from math import sqrt


def get_primes(some_list):
    for num in some_list:
        if num <= 1:
            continue
        for div in range(2, int(sqrt(num)) + 1):
            if num % div == 0:
                break
        else:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))