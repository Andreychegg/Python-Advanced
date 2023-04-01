import re


def my_t9(input_digits):
    letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    with open('words.txt', 'r') as file:
        words = file.read().splitlines()

    pattern = '^' + ''.join('(' + '|'.join(letters[digit]) + ')' for digit in input_digits) + '$'

    result = []
    for word in words:
        if re.match(pattern, word, re.IGNORECASE):
            result.append(word)
    return result


if __name__ == '__main__':
    print(my_t9('22736368'))
