from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello/$', views.hello),
    url(r'^login/$', views.user_login),
    # url(r'^login1/$', views.login1),
    # url(r'^login_render/$', views.login_render),
]
