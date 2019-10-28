#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def filtered_string(strings):
    strings = strings.lower()
    l = 0
    result = []
    res = 0
    result1 = []
    l = re.split(r"['!@#$%^&*()-_+=|\/ 1234567890']", strings)
    for st in l:
        if st != '':
            result.append(st)
    res = "".join(map(str, result))  # type: str
    for index in res:
        result1.append(index)
    return result1


def convert_to_morze(strings):
    azbuka = {'а': '.−',
              'б': '−...',
              'в': '.− −',
              'г': '− − .',
              'д': '−..',
              'е': '.',
              'є': '..−..',
              'ж': '...−',
              'з': '− − ..',
              'и': '−.− −',
              'і': '..',
              'ї': '.− − −.',
              'й': '.− − −',
              'к': '−.−',
              'л': '.−..',
              'м': '− −',
              'н': '−.',
              'о': '− − −',
              'п': '.− −.',
              'р': '.−.',
              'с': '...',
              'т': '−',
              'у': '..−',
              'ф': '..−.',
              'х': '....',
              'ц': '−.−.',
              'ч': '− − −.',
              'ш': '− − − −',
              'щ': '− − . −',
              'ь': '−..−',
              'ю': '..− −',
              'я': '.−.−'}

    strings = filtered_string(strings)
    result = []

    for element in strings:
        result.append(azbuka[element])
    return result


ms = raw_input("input youre message:  ")
print convert_to_morze(ms)
