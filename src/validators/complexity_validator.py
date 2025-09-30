import re
from .length_validator import ValidationResult

def validate_complexity(password: str) -> ValidationResult:
    """Проверка сложности пароля"""
    errors = []
    
    # Проверка на наличие цифр
    if not re.search(r'\d', password):
        errors.append("хотя бы одну цифру")
    
    # Проверка на наличие букв в верхнем регистре
    if not re.search(r'[A-Z]', password):
        errors.append("хотя бы одну заглавную букву")
    
    # Проверка на наличие букв в нижнем регистре
    if not re.search(r'[a-z]', password):
        errors.append("хотя бы одну строчную букву")
    
    # Проверка на наличие специальных символов
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("хотя бы один специальный символ")
    
    if errors:
        return ValidationResult(
            False,
            f"Пароль должен содержать {', '.join(errors)}"
        )
    
    return ValidationResult(True)