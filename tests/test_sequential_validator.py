import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from validators.sequential_validator import has_sequential_chars

class TestSequentialValidator:
    
    def test_has_sequential_chars_detected_ascending(self):
        # Arrange
        password = "abc123"
        
        # Act
        result = has_sequential_chars(password, max_sequential=3)
        
        # Assert
        assert result == True
    
    def test_has_sequential_chars_detected_descending(self):
        # Arrange
        password = "321cba"
        
        # Act
        result = has_sequential_chars(password, max_sequential=3)
        
        # Assert
        assert result == True
    
    def test_has_sequential_chars_not_detected(self):
        # Arrange
        password = "randomPass"
        
        # Act
        result = has_sequential_chars(password, max_sequential=3)
        
        # Assert
        assert result == False
    
    def test_has_sequential_chars_short_password(self):
        # Arrange
        password = "ab"
        
        # Act
        result = has_sequential_chars(password, max_sequential=3)
        
        # Assert
        assert result == False