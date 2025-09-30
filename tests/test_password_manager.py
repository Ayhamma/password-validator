import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.password_manager import PasswordManager

class TestPasswordManager:
    
    def test_password_manager_strong_password(self):
        # Arrange
        manager = PasswordManager()
        strong_password = "My$trongPass999"  # Изменили с 123 на 999
        
        # Act
        result = manager.validate_password(strong_password)
        
        # Assert
        assert result.is_valid == True
        assert len(result.errors) == 0
    
    def test_password_manager_weak_password_multiple_errors(self):
        # Arrange
        manager = PasswordManager()
        weak_password = "123"  # Короткий, простой, популярный
        
        # Act
        result = manager.validate_password(weak_password)
        
        # Assert
        assert result.is_valid == False
        assert len(result.errors) >= 2
    
    def test_password_manager_common_password(self):
        # Arrange
        manager = PasswordManager()
        common_password = "password"
        
        # Act
        result = manager.validate_password(common_password)
        
        # Assert
        assert result.is_valid == False
        # Проверяем что есть ошибка про распространенный пароль
        common_errors = [error for error in result.errors if "распространен" in error]
        assert len(common_errors) > 0
    
    def test_password_manager_sequential_chars(self):
        # Arrange
        manager = PasswordManager()
        sequential_password = "abcd1234WXYZ"  # Явные последовательности 4+ символов
        
        # Act
        result = manager.validate_password(sequential_password)
        
        # Assert
        assert result.is_valid == False
        # Проверяем что есть ошибка про последовательные символы
        sequential_errors = [error for error in result.errors if "последовательные" in error]
        assert len(sequential_errors) > 0