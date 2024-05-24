from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_session),
    path('access/', views.access_session),
]