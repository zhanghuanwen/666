from django.http import JsonResponse
import json
from . import models
from utils.utils_token import *
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def login(request):
    if request.method=='POST':
        data=json.loads(request.body)
        print(data)
        res=models.regist.objects.filter(tel=data['tel'],password=data['password'])
        if len(res) and check_password(data['password'], res[0].password):
            id=res[0].id
            resp=JsonResponse({"id":id},status=200,charset='utf-8',content_type='application/json')
            # 生成token
            resp['token']=send_token(id)
            resp["Access-Control-Expose-Headers"] = "token"
            return resp
        else:
            return JsonResponse({"code":"402"})

def show(request,myid):
    pass

def regist(request):
    if request.method=='POST':
       data=json.loads(request.body)
       print(data)
       user=models.regist.objects.filter(tel=data['tel'])
       # 号码已被注册
       if len(user):
           return JsonResponse({"code":"402"})
       else:
            data['password']=make_password(data["password"],'pbkdf2_sha256')
            res=models.regist.objects.create(**data)
            print(res.id)
            if res.id:
                resp = JsonResponse({"id":res.id}, status=200, charset='utf-8', content_type='application/json')
                # 生成token
                resp['token'] = send_token(res.id)
                resp["Access-Control-Expose-Headers"] = "token"
                return resp
            # 插入数据失败
            else:
                return JsonResponse({"code":"403"})

def insert(request):
    try:
        with open('hnMess.json') as fp:
            users=json.load(fp)
            for user in users:
                # sex=models.sex_li.objects.get(sex=user["sex"])
                # income=models.income_li.objects.filter(income=user['income'])
                # edu=models.edu_li.objects.filter(edu=user['edu'])
                # user["sex"]=sex
                # user["income"]=income[0] if income else None
                # user['edu']=edu[0] if edu else None
                res=models.message.objects.create(**user)
                print(res.id)

            return JsonResponse({"code":"001"})
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "002"})

def getuser(request):
    userid=request.GET.get('id')
    print(userid)
    user=models.base.objects.filter(id=userid)
    if len(user):
        return JsonResponse({"name":user[0].name,"img_src":user[0].img_src})
    else:
        return JsonResponse({"name":userid})