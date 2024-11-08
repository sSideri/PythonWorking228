from lesson_3 import UserService, User

user = UserService()

user_service = User(name='Isko', email='iskoGao@gmail.com', age=300)
UserService.add_user(user_service)

find = user.find_user_by_email('iskoGao@gmail.com')
if find:
    print(f'Пользователь найден: {find.name}, {find.email}, {find.age}')
    
delet = user.delete_user_by_email('iskoGao@gmail.com')
if delet:
    print('Успешно удалено')