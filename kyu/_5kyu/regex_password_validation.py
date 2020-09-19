import re


def validate_password(s):
    return bool(re.search(r'^(?!.*[\W_])(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[\w\d]{6,}', s))
