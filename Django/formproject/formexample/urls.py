from django.urls import path
from . import views

urlpatterns = [
    # path("", views.view_function, name='home'),
    path("", views.valid_function, name='submit'),
]