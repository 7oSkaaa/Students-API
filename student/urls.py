from django.urls import path
from .views import *

urlpatterns = [
    path('', get_post),
    path('<int:id>/', put_delete),
]