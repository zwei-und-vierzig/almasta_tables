from django.conf.urls import url, include
from tables import views

import tables

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new_obj.json$', views.new_object_json, name='new_o_json'),
    url(r'^my_obj.json$', views.my_object_json, name='my_o_json'),
    url(r'^new/get_obj.json', views.get_new_obj),
    url(r'^ChangeStatus.json', views.ChangeStatus),
    url(r'^new/', views.get_new, name='get_new'),
    url(r'^accounts/login/$',  views.login),
    url(r'^accounts/auth/$',  views.auth_view),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/loggedin/$', views.loggedin),
    url(r'^accounts/invalid/$', views.invalid_login),
]