""" создать функцию которая бы находила незакрытые тэги """


import re

"<div>abc</div><p><em><i>test test test</b></em></p>"
# data = re.findall(r'/?\w+', '<<div>abc</div><p><em><i>test test test</b></em></p>')
data = re.findall(r'/?\w+', '<div><div><b></b></div></p>')


open_tags = ['b', 'i', 'em', 'div', 'p']
closed_tags = ['/b', '/i', '/em', '/div', '/p']
for elem in data[:]:
    if elem not in open_tags and elem not in closed_tags:
        data.remove(elem)

for tag in data[:]:
    if '/'+tag not in data[:]:
        # print('---')
        if '/' not in  tag: 
            print(tag)
    else:
        data.remove(tag)
        data.remove('/'+tag)
