import fastapi
from fastapi.requests import Request

from viewmodels.account.accountviewmodel import AccountViewModel
from viewmodels.account.loginviewmodel import LoginViewModel
from viewmodels.account.registerviewmodel import RegisterViewModel


router = fastapi.APIRouter()


@router.get('/account')
def index(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get('/account/register')
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()

@router.get('/account/login')
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()
    

@router.get('/account/logout')
def logout(request: Request):
    return {}
