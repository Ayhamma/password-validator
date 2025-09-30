import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from validators.common_passwords import is_common_password

class TestCommonPasswords:
    
    def test_is_common_password_true(self):
        # Arrange
        common_password = "password"
        
        # Act
        result = is_common_password(common_password)
        
        # Assert
        assert result == True
    
    def test_is_common_password_false(self):
        # Arrange
        unique_password = "MyUniquePassw0rd!"
        
        # Act
        result = is_common_password(unique_password)
        
        # Assert
        assert result == False
    
    def test_is_common_password_case_insensitive(self):
        # Arrange
        common_password_variations = ["PASSWORD", "Password", "PaSsWoRd"]
        
        # Act & Assert
        for variation in common_password_variations:
            result = is_common_password(variation)
            assert result == True