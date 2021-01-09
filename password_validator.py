import string


def validate(password):
    digits = string.digits
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special_symols = '!@#$%^&*()-+={[}]\:;<,>.?/'
    if 8 > len(password):
        return 1
    status = 0
    for c in password:
        if c in upper:
            status = status + 1
            break
    if status == 0:
        return 2
    status = 0
    for c in password:
        if c in lower:
            status = status + 1
            break
    if status == 0:
        return 3
    status = 0
    for c in password:
        if c in digits:
            status = status + 1
            break
    if status == 0:
        return 4
    status = 0
    for c in password:
        if c in special_symols:
            status = status + 1
            break
    if status == 0:
        return 5
    return 0


