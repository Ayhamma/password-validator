from dataclasses import dataclass
from typing import List
from .validators.length_validator import validate_length
from .validators.complexity_validator import validate_complexity
from .validators.common_passwords import is_common_password
from .validators.sequential_validator import has_sequential_chars

@dataclass
class PasswordValidationResult:
    is_valid: bool
    errors: List[str]

class PasswordManager:
    def __init__(self, min_length: int = 8, max_length: int = 64):
        self.min_length = min_length
        self.max_length = max_length
    
    def validate_password(self, password: str) -> PasswordValidationResult:
        """Основная функция валидации пароля"""
        errors = []
        
        # Валидация длины
        length_result = validate_length(password, self.min_length, self.max_length)
        if not length_result.is_valid:
            errors.append(length_result.error_message)
        
        # Валидация сложности
        complexity_result = validate_complexity(password)
        if not complexity_result.is_valid:
            errors.append(complexity_result.error_message)
        
        # Проверка на популярный пароль
        if is_common_password(password):
            errors.append("Пароль слишком распространен")
        
        # Проверка на последовательные символы (только 4+ символов)
        if has_sequential_chars(password, max_sequential=4):
            errors.append("Пароль содержит последовательные символы")
        
        return PasswordValidationResult(len(errors) == 0, errors)