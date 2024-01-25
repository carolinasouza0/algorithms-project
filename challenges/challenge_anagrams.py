def custom_sort(string):
    if len(string) <= 1:
        return string
    middle = len(string) // 2
    left = custom_sort(string[:middle])
    right = custom_sort(string[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return custom_sort(first_string), custom_sort(second_string), False

    first_lower = custom_sort([letter for letter in first_string.lower()])
    second_lower = custom_sort([letter for letter in second_string.lower()])

    return (
        "".join(first_lower),
        "".join(second_lower),
        first_lower == second_lower,
    )
