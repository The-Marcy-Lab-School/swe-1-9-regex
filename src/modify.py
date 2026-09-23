def swap_all_cases(text):
    result = ""
    for char in text:
        is_uppercase_letter = char == char.upper()
        result += char.lower() if is_uppercase_letter else char.upper()

    return result
