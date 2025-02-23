import string
from password.new_password import generate_password
import pytest

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test1():
    password1 = generate_password(10)
    password2 = generate_password(10)
    assert password1 != password2

print(test1())