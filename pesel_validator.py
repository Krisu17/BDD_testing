import string


def validate(pesel):
    if 0 <= len(pesel) or len(pesel) > 11:
        return 1

    for c in pesel:
        if c not in string.digits:
            return 2

    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = 0
    for i in range(10):
        suma += wagi[i] * pesel[i]

    if pesel[10] == suma % 10:
        return 0
    else:
        return 3
