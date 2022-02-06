from django.urls import path
from official.views import *

app_name = 'official'

urlpatterns = [
    path('', index,name="index"),

    path('deletempl/<str:id>',deletempl,name="deletempl"),
]