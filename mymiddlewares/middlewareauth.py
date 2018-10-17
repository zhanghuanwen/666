from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import json

# 自定义中间件
class RequestAuth(MiddlewareMixin):
    def process_request(self, request):
        print(111111)
        if request.method=='POST':
            tel=json.loads(request.body)['tel']
            if not tel:
                return HttpResponse('Sorry')


    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('444')
        pass
    def process_exception(self, request, exception):
        print('555')
        return HttpResponse(exception)
    def process_response(self, request, response):
        print('666')
        return response