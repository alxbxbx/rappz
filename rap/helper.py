__author__ = 'Alxbxbx'

def format_number(number):
    str_number = str(number)
    formatted = ''
    count = 0
    for i in range(len(str_number), 0, -1):
        if count > 2:
            formatted += '.'
            count = 0
        formatted += str_number[i-1]
        count += 1
    formatted = formatted[::-1]
    return formatted

