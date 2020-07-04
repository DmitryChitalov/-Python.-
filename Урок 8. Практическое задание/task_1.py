import hashlib


def substrcounter(preset_string, elements):
    encoded_string = set()
    for el in range(elements):
        if el == 0:
            elements = len(preset_string) - 1
        else:
            elements = len(preset_string)
        for i in range(elements, el, -1):
            print(preset_string[el:i])
        encoded_string.add(
            hashlib.sha1(
                preset_string[el:i].encode('utf-8')
            ).hexdigest())
    return encoded_string


preset_string = 'data'
elements = len(preset_string)


print(f'The number of '
      f'different substrings in string '
      f'{preset_string} is '
      f'{len(substrcounter(preset_string, elements))}')
