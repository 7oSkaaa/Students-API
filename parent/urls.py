from django.urls import path
from .views import *

urlpatterns = [
    path('', ParentView.as_view()),
    path('<int:pk>', ParentDetailView.as_view()),
]