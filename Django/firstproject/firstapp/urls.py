from . import views
from django.urls import path

urlpatterns = [
    path("<str:month>", views.monthly_reward, name="base-url-for-month-name"),
    path("", views.monthly_reward_list)
]