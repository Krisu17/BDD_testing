import string


def validate(pesel):
    if len(pesel) != 11:
        return "1"

    for c in pesel:
        if c not in string.digits:
            return "2"

    wagi = [9, 7, 3, 1, 9, 7, 3, 1, 9, 7]
    suma = 0
    for i in range(10):
        suma += wagi[i] * int(pesel[i])

    if int(pesel[10]) == suma % 10:
        return "0"
    else:
        return "3"
