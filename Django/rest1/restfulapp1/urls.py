from django.urls import path
from .views import BioDataListCreate

urlpatterns = [
    path('biodata/', BioDataListCreate.as_view(), name='bio-data-list-create')
]