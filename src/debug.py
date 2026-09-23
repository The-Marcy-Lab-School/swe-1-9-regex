import re


def is_valid_company_username(username, first_name, last_name):
    pattern = rf"^(sales|tech)\d\w-{first_name[0]}{last_name}\d?$"
    # print(pattern)  # to help you debug, look at the final pattern
    return bool(re.fullmatch(pattern, username))
