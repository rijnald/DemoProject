# demoapp2 views

# from django.conf.urls import urls
from django.urls import path,re_path
from DemoApp2 import views

urlpatterns=[
    path('third/',views.f3),
    path('fourth/',views.f4),
]