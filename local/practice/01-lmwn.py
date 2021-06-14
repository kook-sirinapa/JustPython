from typing import Text


def fn(input):
    pair = {
        '}': '{',
        ')': '(',
        ']': '['
        }
    start_pair = pair.values()
    end_pair = pair.keys()
    temp = []
    for i in input:
        if i in start_pair:
            temp.append(i)
            return 0
    else:
        return str('Oh no')
result = fn('-')
print(result) 