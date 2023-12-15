from fastapi import Body, APIRouter, HTTPException, status, Depends, Request, Response
router = APIRouter(tags=["auth"])
user_coll = [{"username": "admin1", "password": "admin123"},
             {"username": "admin2", "password": "admin456"}]
access_token = "vuhrvjrvr"


@router.post('/api/v1/auth/signup')
def signup(user_data: dict = Body(...)):
    for user_obj in user_coll:
        if user_obj['username'] == user_data['username']:
            # user exists throw error
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="user " + user_obj['username'] + " already signed up!")
    # user doesnt exist
    user_coll.append(user_data)
    return {'user signedup successfully!'}


def generate_token() -> str:
    return access_token


def validate_token(request: Request, user_data: dict = Body(...)) -> bool:
    # 'cookie': 'access_token=vuhrvjrvr'
    headers = request.headers
    print(headers)
    token = ''
    if 'cookie' in headers:
        cookie_value = headers['cookie']
        print(cookie_value)
        if "=" in cookie_value:
            token = cookie_value.split("=")[1]
            print(token)
    return access_token == token


@router.post('/api/v1/auth/signin')
def signin(response: Response, user_data: dict = Body(...)):
    for user_obj in user_coll:
        if user_obj['username'] == user_data['username'] and user_obj['password'] == user_data['password']:
            # user exists and passwords match - generate token
            token = generate_token()
            response.set_cookie('access_token', token)
            return {"access_token": token, "expires_in": 20}
    # user doesnt exist
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="invalid username or password")


@router.post('/api/v1/auth/signout')
def signout(response: Response, user_data: dict = Body(...)):
    response.delete_cookie('access_token')
    return {"access_token": None, "expires_in": 0}


@router.get('/api/v1/auth/users')
def getAllUsers():
    return user_coll


@router.post('/api/v1/users/hello/{username}')
def secured_resource(isValid: bool = Depends(validate_token),user_data: dict = Body(...)):
    if isValid:
        return "hello here is your password "
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="token is invalid")