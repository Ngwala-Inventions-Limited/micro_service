from django.urls import path
from .views import *

urlpatterns = [
    path("get_trans/", get_trans),
    path("get_user/", get_user),
]
