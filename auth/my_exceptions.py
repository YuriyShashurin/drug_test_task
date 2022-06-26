

class UserNotFoundError(Exception):
    """Объект ошибки "Пользователь остутствует в БД"""
    
    def __init__(self, value):
       self.id = value
       self.text = ''
       self.status = 404


    def get_error_text(self):
        self.text = f'Пользователь с id #{self.id} в БД не найден'
        return 

    def __str__(self):
        return f'Пользователь с id #{self.id} в БД не найден'