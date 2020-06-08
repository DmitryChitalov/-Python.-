"""
Задание 2. Выполнить логические побитовые операции "И", "ИЛИ"
и др. над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.

Подсказка: это стандартные операции, которые осуществляются с помощью
стандартных операторов. Попробуйте найти каких именно.
"""
n1 = 5
n2 = 6

print(f'Побитовое AND - {n1&n2}\n'
      f'Побитовое OR - {n1|n2}\n'
      f'Побитовое XOR - {n1^n2}\n'
      f'Побитовое NOT {n1} - {~n1}\n'
      f'Побитовое NOT {n2} - {~n2}\n'
      f'Побитовый сдвиг "{n1}" вправо на два знака - {n1 >> 2}\n'
      f'Побитовый сдвиг "{n1}" влево на два знака - {n1 << 2}')
