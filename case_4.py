""" создать функцию которая бы находила незакрытые тэги """

import re

"<div>abc</div><p><em><i>test test test</b></em></p>"


# data = re.findall(r'/?\w+', ''<div><div><b></b></div></p>'')
def html_elements(value="<div>abc</div><p><em><i>test test test</b></em></p>"):
    data = re.findall(r'/?\w+', value)
    open_tags = ['b', 'i', 'em', 'div', 'p']
    closed_tags = ['/b', '/i', '/em', '/div', '/p']
    result = 0
    for elem in data[:]:
        if elem not in open_tags and elem not in closed_tags:
            data.remove(elem)

    for tag in data[:]:
        if '/' + tag not in data:
            if '/' not in tag:
                result = ''.join(tag)
        else:
            data.remove(tag)
            data.remove('/' + tag)

    return result


if __name__ == '__main__':
    print(html_elements())
