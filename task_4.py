"""
Задание 4.
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

# 1 способ
dict_logins = {'alex' : ['Password1', False],  'bob' : ['Password2', False], 'john' : ['Password3', True], 'helen' : ['Password4', True]}
login = input('Please provide login: ').lstrip().rstrip().lower()
password = input('Please provide password: ').lstrip().rstrip()

def authentificate (login, password):
    login_info = dict_logins.get(login)
    if login_info[0] != password:
        print(f'You pvided wrong password. Bye')
        return
    if dict_logins.get(login)[1] == False:
        answer_activate = input(f'You should acvate you login. Do it? Yes/No: ').lower()
        if answer_activate == 'yes':
            login_info[1] = True # activate login
            dict_logins.update({login:login_info}) # put info dict 
    else:
        print(f'You login {login} is activated. Welcome.')
    return    

authentificate (login, password)
print(dict_logins)

# 2 способ
# не придумал 

