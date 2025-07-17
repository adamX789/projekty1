"""functions to sort a word/number list
    """


def sort_words(word_list):
    sorted_list = []
    for i in range(len(word_list)):
        word_list[i] = word_list[i].lower()
    while word_list:
        minimum = word_list[0]
        for word in word_list:
            if word < minimum:
                minimum = word
        sorted_list.append(minimum)
        word_list.remove(minimum)
    return sorted_list


def sort_numbers(num_list):
    sorted_list = []
    while num_list:
        minimum = num_list[0]
        for num in num_list:
            if num < minimum:
                minimum = num
        sorted_list.append(minimum)
        num_list.remove(minimum)
    return sorted_list


def reverse_sort_words(word_list):
    sorted_list = []
    for i in range(len(word_list)):
        word_list[i] = word_list[i].lower()
    while word_list:
        maximum = word_list[0]
        for word in word_list:
            if word > maximum:
                maximum = word
        sorted_list.append(maximum)
        word_list.remove(maximum)
    return sorted_list


def reverse_sort_numbers(num_list):
    sorted_list = []
    while num_list:
        maximum = num_list[0]
        for num in num_list:
            if num > maximum:
                maximum = num
        sorted_list.append(maximum)
        num_list.remove(maximum)
    return sorted_list
