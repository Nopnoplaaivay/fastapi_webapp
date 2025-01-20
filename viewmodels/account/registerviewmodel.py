from typing import Optional
from starlette.requests import Request

from viewmodels.shared.viewmodel import ViewModelBase

class RegisterViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.name: Optional[str] = None
        self.email: Optional[str] = None
        self.password: Optional[str] = None

    async def load(self):
        form = await self.request.form()
        self.name = form.get('name')
        self.email = form.get('email')
        self.password = form.get('password')
        print(form)

        if not self.name or not self.name.strip():
            self.error = 'You must specify a name.'
        elif not self.email or not self.email.strip():
            self.error = 'You must specify an email.'
        elif not self.password or len(self.password.strip()) < 5:
            self.error = 'You must specify a password and must be at least 5 characters long.'
        