def has_sequential_chars(password: str, max_sequential: int = 4) -> bool:
    """
    Проверка на последовательные символы.
    Считаем последовательностью только 4+ подряд идущих символа.
    """
    if len(password) < max_sequential:
        return False
    
    for i in range(len(password) - max_sequential + 1):
        substring = password[i:i + max_sequential]
        
        # Проверка последовательных цифр (только 4+ символов)
        if substring.isdigit():
            digits = [int(ch) for ch in substring]
            if all(digits[j] + 1 == digits[j + 1] for j in range(len(digits) - 1)):
                return True
            if all(digits[j] - 1 == digits[j + 1] for j in range(len(digits) - 1)):
                return True
        
        # Проверка последовательных букв (только 4+ символов)
        if substring.isalpha() and substring.islower():
            chars = [ord(ch) for ch in substring]
            if all(chars[j] + 1 == chars[j + 1] for j in range(len(chars) - 1)):
                return True
        
        if substring.isalpha() and substring.isupper():
            chars = [ord(ch) for ch in substring]
            if all(chars[j] + 1 == chars[j + 1] for j in range(len(chars) - 1)):
                return True
    
    return False