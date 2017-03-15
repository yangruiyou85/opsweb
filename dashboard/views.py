# -*- coding:utf-8 -*-

from django.http import HttpResponse, JsonResponse
import json
from django.template import Context, loader


def login(request):
    template = loader.get_template('login.html')
    context = Context({'title': '5262运维平台'})
    return HttpResponse(template.render(context))


# Create your views here.
def hello(request):
    data = {"name": "5262.com", "age": 3}
    data_list = ["shenzhen", "beijing", "hanshou"]
    # return JsonResponse(data)
    return JsonResponse(data_list, safe=False)
    # return HttpResponse(json.dumps(data),content_type="application/json")
    # return HttpResponse('<h1>hello world.深圳你好.</h1>')
