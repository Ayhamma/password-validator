from dataclasses import dataclass
from typing import Optional

@dataclass
class ValidationResult:
    is_valid: bool
    error_message: str = ""

def validate_length(password: str, min_length: int = 8, max_length: Optional[int] = None) -> ValidationResult:
    """Валидация длины пароля"""
    if len(password) < min_length:
        return ValidationResult(
            False, 
            f"Пароль должен содержать минимум {min_length} символов"
        )
    
    if max_length and len(password) > max_length:
        return ValidationResult(
            False,
            f"Пароль должен содержать не более {max_length} символов"
        )
    
    return ValidationResult(True)