import string
import pytest
from password.new_password import generate_password

# Test that the generated password contains only valid characters
def test_password_characters():
    """Test that only valid characters are used in the generated password"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Generate a longer password for better testing
    for char in password:
        assert char in valid_characters

# Test that the length of the generated password matches the requested length
def test_password_length():
    """Test that the generated password has the correct length"""
    password_length = 12
    password = generate_password(password_length)
    assert len(password) == password_length

# Test that two generated passwords are different
def test_password_uniqueness():
    """Test that two consecutive passwords are different"""
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2

# Additional test: Test that a very long password is generated correctly
def test_long_password():
    """Test that a password with a very long length is generated correctly"""
    password_length = 1000
    password = generate_password(password_length)
    assert len(password) == password_length
    for char in password:
        assert char in string.ascii_letters + string.digits + string.punctuation

# Additional test: Test empty password length argument (default 12)
def test_default_password_length():
    """Test that the default password length is 12 if no argument is provided"""
    password = generate_password()
    assert len(password) == 12
