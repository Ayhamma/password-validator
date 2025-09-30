import os

def load_common_passwords() -> set:
    """Загрузка списка популярных паролей из файла"""
    common_passwords = {
        "password", "123456", "12345678", "1234", "qwerty", 
        "admin", "letmein", "welcome", "monkey", "password1"
    }
    
    # Попытка загрузить из файла, если он существует
    file_path = os.path.join(os.path.dirname(__file__), '../../data/common_passwords.txt')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            common_passwords.update(line.strip() for line in f if line.strip())
    
    return common_passwords

def is_common_password(password: str) -> bool:
    """Проверка, является ли пароль популярным"""
    common_passwords = load_common_passwords()
    return password.lower() in common_passwords