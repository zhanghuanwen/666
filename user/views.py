from django.http import JsonResponse
import json
from . import models
from utils.utils_token import *
from utils.datetransform import *
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
import math

# Create your views here.

# 登录
def login(request):
    if request.method=='POST':
        try:
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
        except Exception as ex:
            print(ex)
            return JsonResponse({"code":"409"})

def show(request,myid):
    pass

# 注册
def regist(request):
    if request.method=='POST':
        try:
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
        except Exception as ex:
            print(ex)
            return JsonResponse({"code":"409"})



# 首页加载时获取用户信息
def getuser(request):
    try:
        userid=request.GET.get('id')
        print(userid)
        user=models.base.objects.filter(id=userid)
        if len(user):
            return JsonResponse({"name":user[0].name,"img_src":user[0].img_src,"sex_id":user[0].sex_id,"city":user[0].city})
        else:
            return JsonResponse({"name":userid})
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "409"})

# 首页加载时获取推荐用户
def index_users(request):
    try:
        sex_id=request.GET.get('sex_id')
        print(sex_id)
        if sex_id:
            users = models.base.objects.exclude(sex_id=sex_id)[0:10].values('id','name', 'birth', 'height','sex_id','img_src')
        else:
            users=models.base.objects.filter()[0:10].values('id','name','birth','height','sex_id','img_src')
        users=dateToage(users)
        print(len(users))
        return JsonResponse(users,safe=False)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "409"})

# 同城人
def getcity(request):
    try:
        city=request.GET.get('city')
        sex_id=request.GET.get('sex_id')
        print(city)
        users=models.base.objects.filter(city__contains=city).values('id','name', 'birth', 'height','sex_id','img_src','city')
        new_users=[]
        for user in users:
            if user['sex_id'] != int(sex_id):
                new_users.append(user)
        if len(new_users)>10:
            new_users=new_users[0:10]
        new_users=dateToage(new_users)
        return JsonResponse(new_users,safe=False)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "409"})
#     爱电影
def getfilm(request):
    try:
        hobbys=models.hobby.objects.exclude(film='')
        sex_id=request.GET.get('sex_id')
        print(len(hobbys))
        users=[]
        for hobby in hobbys:
            user= models.base.objects.filter(id=hobby.id).values('id', 'name', 'birth', 'height', 'sex_id','img_src')
            if user[0]['sex_id'] != int(sex_id):
                users.append(user[0])
        if len(users)>10:
            users=users[0:10]
        users=dateToage(users)
        return JsonResponse(users,safe=False)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "409"})

#     爱美食
def getfood(request):
    try:
        hobbys=models.hobby.objects.exclude(food='')
        sex_id=request.GET.get('sex_id')
        print(len(hobbys))
        users=[]
        for hobby in hobbys:
            user= models.base.objects.filter(id=hobby.id).values('id', 'name', 'birth', 'height', 'sex_id','img_src')
            if user[0]['sex_id'] != int(sex_id):
                users.append(user[0])
        if len(users)>10:
            users=users[0:10]
        users=dateToage(users)
        return JsonResponse(users,safe=False)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "409"})

#     爱宠物
def getpet(request):
    try:
        hobbys=models.hobby.objects.exclude(pet='')
        sex_id=request.GET.get('sex_id')
        print(len(hobbys))
        users=[]
        for hobby in hobbys:
            user= models.base.objects.filter(id=hobby.id).values('id', 'name', 'birth', 'height', 'sex_id','img_src')
            if user[0]['sex_id'] != int(sex_id):
                users.append(user[0])
        if len(users)>10:
            users=users[0:10]
        users=dateToage(users)
        return JsonResponse(users,safe=False)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "409"})

#     90后
def get90(request):
    try:
        users=models.base.objects.filter(birth__gte='1990-1-1').values('id', 'name', 'birth', 'height', 'sex_id','img_src', 'city')
        sex_id=request.GET.get('sex_id')
        new_users = []
        for user in users:
            if user['sex_id'] != int(sex_id):
                new_users.append(user)
        if len(new_users) > 10:
            new_users = new_users[0:10]
        new_users = dateToage(new_users)
        return JsonResponse(new_users, safe=False)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "409"})

# 搜索页加载时
def search_users(request):
    try:
        con=request.GET.get('con')
        sex_id=request.GET.get('sex_id')
        index=int(request.GET.get('index'))
        pages=20
        print(con,index,1111111111111)
        # 已登录
        if sex_id:
            if con:
                users=models.base.objects.filter(Q(city__contains=con)|Q(signature__contains=con)|Q(edu__edu__contains=con),~Q(sex_id=sex_id))\
                    .values('id','name','birth','city','signature','img_src','height','income_id')
                if len(users)>20:
                    pagescount=math.ceil(len(users)/pages)
                    users=users[(pages*(index-1)):(pages*index)]
                elif len(users)==0:
                    users= models.base.objects.filter(~Q(sex_id=sex_id)).values('id','name', 'birth', 'city', 'signature','img_src','height','income_id')
                    pagescount=math.ceil(len(users)/pages)
                    users=users[(pages*(index-1)):(pages*index)]
                else:
                    pagescount=math.ceil(len(users)/pages)
            else:
                users = models.base.objects.filter(~Q(sex_id=sex_id)).values('id','name', 'birth', 'city', 'signature','img_src','height','income_id')
                pagescount = math.ceil(len(users) / pages)
                users=users[(pages*(index-1)):(pages*index)]
            users = dateToage(users)
            print(len(users))
            return JsonResponse({"users":users,"pagescount":pagescount},safe=False)
        # 未登录
        else:
            if con:
                users=models.base.objects.filter(Q(city__contains=con)|Q(signature__contains=con)|Q(edu__edu__contains=con))\
                    .values('id','name','birth','city','signature','img_src','height','income_id')
                if len(users)>20:
                    pagescount = math.ceil(len(users) / pages)
                    users=users[(pages*(index-1)):(pages*index)]
                elif len(users)==0:
                    users= models.base.objects.filter().values('id','name', 'birth', 'city', 'signature','img_src','height','income_id')
                    pagescount = math.ceil(len(users) / pages)
                    users=users[(pages*(index-1)):(pages*index)]
                else:
                    pagescount=math.ceil(len(users)/pages)
            else:
                users = models.base.objects.filter().values('id','name', 'birth', 'city', 'signature','img_src','height','income_id')
                pagescount = math.ceil(len(users) / pages)
                users = users[(pages*(index-1)):(pages*index)]
            users = dateToage(users)
            print(len(users))
            return JsonResponse({"users":users,"pagescount":pagescount},safe=False)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code":"409"})

# 点击搜索
def btn_search(request):
    try:
        res=json.loads(request.body)
        print(res)
        pages=20
        index=res["index"]
        users=models.base.objects.filter(sex_id=res['sex'],birth__gte=res['age'],city__contains=res['city'],edu_id=res['edu'],income_id=res['income'])\
            .values('id','name', 'birth', 'city', 'signature', 'img_src', 'height', 'income_id')
        new_users=[]
        for user in users:
            if int(user["height"])<int(res['height']):
                new_users.append(user)
        pagescount = math.ceil(len(users) / pages)
        if len(new_users) > 20:
            new_users = new_users[(pages * (index - 1)):(pages * index)]
        elif len(new_users)==0:
            new_users=models.base.objects.filter(sex_id=res['sex']).values('id','name', 'birth', 'city', 'signature', 'img_src', 'height', 'income_id')
            pagescount = math.ceil(len(new_users) / pages)
            new_users=new_users[(pages * (index - 1)):(pages * index)]
        new_users = dateToage(new_users)
        print(len(new_users))
        return JsonResponse({"users": new_users, "pagescount": pagescount}, safe=False)

    except Exception as ex:
        print(ex)
        return JsonResponse({"code":"409"})

# 用户详情页获取信息
def getuserAll(request):
    try:
        id=request.GET.get('id')
        user_base=models.base.objects.filter(id=id).values('name','birth','height','marry','city','signature','img_src','edu__edu','income__income')
        user_base=dateToage(user_base)
        user_mess=models.message.objects.filter(id=id).values()
        user_life=models.life.objects.filter(id=id).values()
        user_hobby=models.hobby.objects.filter(id=id).values()
        user={
            "user_base":user_base[0],
            "user_mess":list(user_mess)[0],
            "user_life":list(user_life)[0],
            "user_hobby":list(user_hobby)[0]
        }
        return JsonResponse(user)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code":"409"})

