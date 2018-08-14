from django.conf.urls import url
from basic_app import views

#TEMPLATE TAGGING
app_name = 'basic_marja'

urlpatterns = [
    url(r'^relative/$', views.relative, name ='relative'),
    url(r'^other/$', views.others, name = 'other')
]