def palindrome_swapper(value='kyaak'):
    for idx, elem in enumerate(value):
        if idx == len(value) - 1:
            return -1
        string = list(value)
        string[idx], string[idx + 1] = string[idx + 1], string[idx]
        string = ''.join(char for char in string)
        if string == string[::-1]:
            return string


if __name__ == '__main__':
    print(palindrome_swapper())