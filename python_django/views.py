from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import reverse,redirect

def index(request):
    # return HttpResponse('<h1>hello world</h1>')
    return render(request,'index.html')
    # url=reverse('user:show',kwargs={'myid':888})
    # return redirect(url)
