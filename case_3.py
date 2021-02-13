import sys


# def k_unique_characters(value='2aabbcbbbadef'):
def k_unique_characters(value='3aabacbebebe'):
    string = ''.join(value[1:])
    k_qty = int(value[0])
    k_chars = [0] * len(string)
    data, result = [], []
    if len(string) < k_qty or len(set(string)) < k_qty:
        sys.exit('there is no enough unique characters')
    elif len(string) == k_qty and len(set(string)) == k_qty:
        return string
    else:
        for elem in range(len(k_chars)):
            k_chars[elem] = string[elem]
        for idx in range(len(string)):
            data.clear()
            for _while in range(len(string)):
                try:
                    data.append(k_chars[idx])
                except:
                    pass
                idx += 1
                if len(set(data)) > k_qty:
                    data[-1] = ''
                    break
            if len(data) > len(result):
                result = ''.join([char for char in data])

        return result


print(k_unique_characters())
