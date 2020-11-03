"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

admin = {
    'login_name': 'admin_admin',
    'password': 'password',
    'activated': 'no'
}

deamon = {
    'login_name': 'deamon_deamon',
    'password': 'psswrd',
    'activated': 'yes'
}

user = {
    'login_name': 'user_user',
    'password': None,
    'activated': 'no'
}


# Solution_1: полагаю, что здесь будет O(n), т.к. алгоритм решения / переназначения переменных линейный


def sign_in(login, password):

    if login == admin['login_name'] and password == admin['password']:
        print(f'Hey {login}! Welcome back!')
    elif login == deamon['login_name'] and password == deamon['password']:
        print(f'Hey {login}! Welcome back!')
    else:
        answer = input('Your login has been recognised but your profile is not activated yet. \n Want to activate? y/n: ')
        if answer == 'y':
            user['password'] = input('Enter your new password: ')
            user['activated'] = 'yes'
            print('Your profile has been successfully activated!')
        else:
            print('Buy then!')


sign_in('admin_admin', 'password')
sign_in('deamon_deamon', 'psswrd')
sign_in('user_user', None)

print(user)











