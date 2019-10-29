import winsound
import re
import  time


def filtered_string(strings):
    strings = strings.lower()
    l = 0
    result = []
    res = 0
    result1 = []
    l = re.split(r"['!@#$%^&*()-_+=|1234567890]", strings)
    for st in l:
        if st != '':
            result.append(st)
    res = "".join(map(str, result))  # type: str
    for index in res:
        result1.append(index)
    return result1


def convert_to_morze(strings):
    azbuka = {'a': '.-',
              'b': '-...',
              'c': '-.-.',
              'd': '-..',
              'e': '.',
              'f': '..-.',
              'g': '--.',
              'h': '....',
              'i': '..',
              'j': '.---',
              'k': '-.-',
              'l': '.-..',
              'm': '--',
              'n': '-.',
              'o': '---',
              'p': '.--.',
              'q': '--.-',
              'r': '.-.',
              's': '...',
              't': '-',
              'u': '..-',
              'v': '...-',
              'w': '.--',
              'x': '-..-',
              'y': '-.--',
              'z': '--..'}

    strings = filtered_string(strings)
    result = []

    for element in strings:
        result.append(azbuka[element])
    return result


ms = raw_input("input youre message:  ")
mess = convert_to_morze(ms)
frequency = 1000
for i in mess:
    for symbol in i:
        if symbol == '-':
            winsound.Beep(frequency, 1000)
        elif symbol == '.':
            winsound.Beep(frequency, 300)
    print
    time.sleep(0.2)
