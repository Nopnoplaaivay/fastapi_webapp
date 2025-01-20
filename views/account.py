import fastapi
from fastapi.requests import Request
from fastapi_chameleon import template
from starlette import status
from starlette.responses import Response

from infrastructure import cookie_auth
from services import user_service
from viewmodels.account.accountviewmodel import AccountViewModel
from viewmodels.account.loginviewmodel import LoginViewModel
from viewmodels.account.registerviewmodel import RegisterViewModel


router = fastapi.APIRouter()


@router.get('/account')
@template()
def index(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()

'''
REGISTER
'''
@router.get('/account/register')
@template()
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()
    
@router.post('/account/register')
@template()
async def register(request: Request):
    vm = RegisterViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    # Create the account    
    account = user_service.create_account(vm.name, vm.email, vm.password)

    # Login user
    response = fastapi.responses.RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, account.id)
    return response

'''
LOGIN
'''
@router.get('/account/login')
@template()
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()
    
@router.post('/account/login')
@template(template_file='account/login.pt')
async def login_post(request: Request):
    vm = LoginViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    user = user_service.login_user(vm.email, vm.password)
    if not user:
        vm.error = 'The account does not exist or the password is wrong.'
        return vm.to_dict()

    resp = fastapi.responses.RedirectResponse('/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(resp, user.id)

    return resp

'''
LOGOUT
'''
@router.get('/account/logout')
@template()
def logout(response: Response):
    response = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)
    return response