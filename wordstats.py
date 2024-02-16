def average_length(user_string):
    words = user_string.split()
    if words:  # Ensure the string is not empty
        avg = sum(len(word) for word in words) / len(words)
    else:
        avg = 0
    return avg


def word_count(user_string):
    if user_string:
        words = len(user_string.split())
    else:
        words = 0

    return words

def char_count(user_string):
    if user_string:
        chars = len(user_string)
    else:
        chars = 0

    return chars