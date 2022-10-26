from django.urls import path
from .views import *

urlpatterns = [
    path('', SubjectView.as_view()),
    path('<int:pk>', SubjectDetailView.as_view()),
]