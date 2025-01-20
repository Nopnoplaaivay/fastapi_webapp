from typing import Optional
from data.user import User

def user_count() -> int:
    return 6104

def create_account(name: str, email: str, pass_word: str) -> dict:
    return User(name, email, 'pass_word')

def login_user(email: str, pass_word: str) -> Optional[User]:
    if pass_word == 'pass_word':
        return User('test user', email, 'pass_word')
    
    return None