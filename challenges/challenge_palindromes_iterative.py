def is_palindrome_iterative(word):
    if not word:
        return False
    word_inverted = word[::-1]
    return word == word_inverted
