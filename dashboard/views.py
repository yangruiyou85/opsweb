# -*- coding:utf-8 -*-

from django.http import HttpResponse, JsonResponse
import json
from django.template import Context, loader, RequestContext, Template
from django.shortcuts import render
from django.contrib.auth import authenticate, login
#from django.contrib.auth.models import User


def user_login(request):
    # template = loader.get_template('login.html')
    # context = Context({'title': '5262运维平台'})
    # return HttpResponse(template.render(context))
    if request.method == "GET":
        return render(request, 'login.html', {'title': '5262运维平台'})
    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("用户登录成功")
            else:
                return HttpResponse("用户禁用")
        else:
            return HttpResponse("用户登录失败")


def user_logout(request):
    pass


# Create your views here.
def hello(request):
    data = {"name": "5262.com", "age": 3}
    data_list = ["shenzhen", "beijing", "hanshou"]
    # return JsonResponse(data)
    return JsonResponse(data_list, safe=False)
    # return HttpResponse(json.dumps(data),content_type="application/json")
    # return HttpResponse('<h1>hello world.深圳你好.</h1>')


def login1(requst):
    template = loader.get_template('login.html')
    context = RequestContext(requst, {'title': '5262运维平台'})
    return HttpResponse(template.render(context))


def login_render(request):
    return render(request, 'login.html', {'title': '5262运维平台'})
