import re


def checkLogin(login):
    login_length = len(login)
    if login_length < 5:
        return "1"
    checked_login = re.search("^[a-zA-Z]+$", login)
    if checked_login is None:
        return "2"
    return "0"
