def average_length(user_string):
    words = user_string.split()
    if words:  # Ensure the string is not empty
        avg = sum(len(word) for word in words) / len(words)
    else:
        avg = 0
    return avg

def longest_word(user_string):
    words = user_string.split()
    if words:
        long_word_so_far = words[0]
        for word in words:
            if len(word) > len(long_word_so_far):
                long_word_so_far = word
            else:
                pass
    else:
        return "No words found"