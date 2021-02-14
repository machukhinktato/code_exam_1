import re


def time_difference(data=['10:00am', '11:45', '5^00am', '12^01am']):
    """ функция высчитывает меньший временной диапозон в предоставленном списке"""
    time_list = []
    for elem in data:
        if 'pm' in elem:
            time_list.append(handling(elem))
        else:
            time_list.append((handling(elem, status='am')))
    return smallest_diff(sorted(time_list))


def handling(elem, status='pm'):
    match = re.findall(r'\d+', elem)
    if status == 'pm' or int(match[0]) == 12:
        match = int(match[0]) + 12, int(match[1])
    match = int(match[0]) * 60 + int(match[1])
    return match


def smallest_diff(value):
    result = []
    for elem in range(len(value)):
        try:
            result.append(value[elem+1] - value[elem])
        except:
            pass
    return min(result)


if __name__ == '__main__':
    print(time_difference())
