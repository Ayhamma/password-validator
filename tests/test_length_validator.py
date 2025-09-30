import pytest
import sys
import os

# Добавляем src в путь импорта
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from validators.length_validator import validate_length

class TestLengthValidator:
    
    def test_validate_length_correct(self):
        # Arrange
        password = "secure123"
        min_length = 8
        
        # Act
        result = validate_length(password, min_length)
        
        # Assert
        assert result.is_valid == True
        assert result.error_message == ""
    
    def test_validate_length_too_short(self):
        # Arrange
        password = "short"
        min_length = 8
        
        # Act
        result = validate_length(password, min_length)
        
        # Assert
        assert result.is_valid == False
        assert "минимум 8 символов" in result.error_message
    
    def test_validate_length_with_max_limit(self):
        # Arrange
        password = "a" * 65
        min_length = 8
        max_length = 64
        
        # Act
        result = validate_length(password, min_length, max_length)
        
        # Assert
        assert result.is_valid == False
        assert "не более 64 символов" in result.error_message
    
    def test_validate_length_exact_minimum(self):
        # Arrange
        password = "12345678"  # ровно 8 символов
        min_length = 8
        
        # Act
        result = validate_length(password, min_length)
        
        # Assert
        assert result.is_valid == True