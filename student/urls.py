from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentView.as_view()),
    path('<int:pk>', StudentDetailView.as_view()),
]