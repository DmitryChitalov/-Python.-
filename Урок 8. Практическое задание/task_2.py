from collections import Counter, deque


def treezator(args):
    uniq_sym = Counter(args)
    sorted_el = deque(sorted(uniq_sym.items(),
                             key=lambda item: item[1]))
    if len(sorted_el) != 1:
        while len(sorted_el) > 1:
            weight = sorted_el[0][1] + sorted_el[1][1]
            combinated_element = {0: sorted_el.popleft()[0],
                                  1: sorted_el.popleft()[0]}
            for el, uniq_sym in enumerate(sorted_el):
                if weight > uniq_sym[1]:
                    continue
                else:
                    sorted_el.insert(el,
                                     (combinated_element,
                                      weight))
                    break
            else:
                sorted_el.append(
                    (combinated_element, weight)
                )
    return sorted_el[0][0]


encoded_table = dict()


def encoder(args, path=' '):
    if not isinstance(args, dict):
        encoded_table[args] = path
    else:
        encoder(args[0], path=f'{path}0')
        encoder(args[1], path=f'{path}1')


preset_string = 'руку ыщьу вфеф'
encoder(treezator(preset_string))


for el in preset_string:
    print(encoded_table[el], end=' ')

"""
Именно материал этого урока пошел особенно тяжело, в сравнении с остальными.
Долго ковырял примеры, смог сделать копию, изредка подглядывая. Были не очень понятны
телодвижения с Path на 35/36 строках.
"""