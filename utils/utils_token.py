import jwt
from datetime import datetime,timedelta
from functools import wraps

SECRET_KEY='123456'

def send_token(id):
    datetimeInt=datetime.now()+timedelta(hours=1)
    option={
        'iss': 'meetlo.com',  # 签发者
        'exp': datetimeInt,  # 过期时间
        'aud': 'webkit',  # token的接受者，这里指定为浏览器
        'user_id': id  # 放入用户信息，唯一标识
    }
    token = jwt.encode(option, SECRET_KEY, 'HS256').decode()
    return token

def check_token(request,*args):
    def decorated(func):
        @wraps(func)
        def wrapper():
            try:
                token=request.headers['token']
                decoded=jwt.decode(token,SECRET_KEY,audience='webkit',algorithms=['HS256'])
                print(decoded['user_id'])
                return func(decoded['user_id'])
            except jwt.ExpiredSignatureError:
                return 'error1....'
            except Exception:
                return 'error2.....'
        return wrapper
    return decorated