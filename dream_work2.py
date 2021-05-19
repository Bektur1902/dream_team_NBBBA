# # Задание 2:
# Напишите программу Logger.
# Это может быть либо функцией либо методом класса.
# Функция должна делать следующее:
# 1. Принимать Логин, Пароль1 и Пароль2.
# 2. Проверять если Логин меньше 5 символов возвращать пользователю что Логин слишком короткий.
# 3. Если Логин указан верно запустить бесконечный цикл для запроса пароля. Пока пользователь не введёт верный пароль спрашивать снова и снова.
# 4. Проверять если Пароль меньше 8 символов выводить на экран пользователю что Пароль слишком короткий.
# 5. Проверять если Пароль1 НЕ равен Пароль2 выводить на экран пользователю что пароли не совпадают.
# 6. Если все данные верны создайте файл users.txt и запишите туда Логин и Пароль пользователя в формате: Логин: <Логин Пользователя> - Пароль: <Пароль Пользователя>
# 7. Информацию о Всех Успешно Зарегистрированных Пользователей вносите в другой файл log.txt в формате: "Пользователь успешно зарегистрирован <ВРЕМЯ>"
# Время должно быть в формате: <ЧАС>:<МИНУТЫ>:<СЕКУНДЫ>.<ТЫСЯЧНЫЕ СЕКУНДЫ>

from datetime import datetime

def main():
	
	while True:

		login = input('Enter login: ' )
		if check_login(login) == True:
			password1 = input('Enter password_1: ')
			password2 = input('Enter password_2: ')

			if check_passwords(password1, password2) == True:
				break
		
	users(login, password1)
	logs()


def check_login(login):

	if len(login) < 5:
		print('Логин слишком короткий')
		return False
	else: 
		return True

def check_passwords(password1, password2):

	if len(password1) < 8:
		print('Пароль слишком короткий')

	elif password1 != password2:
		print('Пароли не совпадают') 

	else: 
		return True

def users(login, password1):

	with open('users.txt', 'a') as f:
		users = (f"Логин пользователя: {login} Пароль пользователя: {password1}")
		f.write(users + '\n')
	
def logs():
	
	now = datetime.now()

	with open('logs.txt', 'a') as log:
		text = (f"Пользователь успешно зарегистрирован: {now.strftime('%H:%M:%S.%f')}")
		log.write(text + '\n')



main()