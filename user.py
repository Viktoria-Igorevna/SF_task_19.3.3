import requests
import config

# Регистрирует пользователя в системе
res_1 = requests.get(f'{config.URL}/user/login', headers={'username': config.username, 'password': config.password})
print(res_1.text)

# Создает пользователя
res_2 = requests.post(f'{config.URL}/user', json={
    "id": 5,
    "username": config.username,
    "firstName": 'Viktoria',
    "lastName": "Bystrova",
    "email": "vika_bystrova@gmail.com",
    "password": config.password,
    "phone": '8991234567',
    "userStatus": 0
})
print(res_2.text)

# Находит пользователя по имени
res_3 = requests.get(f'{config.URL}/user/{config.username}')
print(res_3.text)

# Обновляет данные пользователя
res_4 = requests.put(f'{config.URL}/user/{config.username}', json={
    "id": 9223372036854758000,
    "username": config.username,
    "firstName": 'Vikaa',
    "lastName": "Bystrova",
    "email": "viktoria_bystrova@gmail.com",
    "password": config.password,
    "phone": '+79887776543',
    "userStatus": 0
})
print(res_4.text)

res_5 = requests.delete(f'{config.URL}/user/{config.username}')
print(res_5.text)

