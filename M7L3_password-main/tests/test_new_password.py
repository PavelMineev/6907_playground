import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Тест, что длина пароля соответствует заданной"""
    for length in [8, 12, 16, 20]:  # Проверяем разные длины
        password = generate_password(length)
        assert len(password) == length

def test_password_uniqueness():
    """Тест, что два сгенерированных подряд пароля различаются"""
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2

def test_password_complexity():
    """Тест, что пароль содержит буквы, цифры и специальные символы"""
    password = generate_password(20)
    
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    assert has_letter and has_digit and has_special


