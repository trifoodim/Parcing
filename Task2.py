#  найти те слова, которые встречаются чаще всего,
#  и вывести их в алфавитном порядке,
#  разделяя пробелами.

import re
from collections import Counter
from urllib.request import urlopen

html = urlopen('https://ru.wikipedia.org/wiki/Python').read().decode('utf-8')
expr = '<code>(.*?)</code>'
l = sorted(re.findall(expr, html))
print(Counter(l))