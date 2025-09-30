import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from validators.complexity_validator import validate_complexity

class TestComplexityValidator:
    
    def test_validate_complexity_strong_password(self):
        # Arrange
        password = "SecurePass123!"
        
        # Act
        result = validate_complexity(password)
        
        # Assert
        assert result.is_valid == True
    
    def test_validate_complexity_no_digits(self):
        # Arrange
        password = "NoDigitsHere!"
        
        # Act
        result = validate_complexity(password)
        
        # Assert
        assert result.is_valid == False
        assert "цифру" in result.error_message
    
    def test_validate_complexity_no_uppercase(self):
        # Arrange
        password = "nouppercase123!"
        
        # Act
        result = validate_complexity(password)
        
        # Assert
        assert result.is_valid == False
        assert "заглавную букву" in result.error_message
    
    def test_validate_complexity_no_special_chars(self):
        # Arrange
        password = "NoSpecialChars123"
        
        # Act
        result = validate_complexity(password)
        
        # Assert
        assert result.is_valid == False
        assert "специальный символ" in result.error_message