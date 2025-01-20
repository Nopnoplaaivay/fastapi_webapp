from starlette.requests import Request

from data.user import User
from viewmodels.shared.viewmodel import ViewModelBase

class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.user = User(name="Michael", email="michael6104@gmail.com", hash_password="123456")