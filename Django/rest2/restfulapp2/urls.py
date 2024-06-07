from django.urls import path, include

# PART A 

'''
from .views import index

urlpatterns = [
    path('index/', index),
]
'''

# PART B

'''
from .views import PersonAPI

urlpatterns = [
    path('person/', PersonAPI),
]
'''

# PART C

'''
from .views import PersonAPI, login

urlpatterns = [
    path('person/', PersonAPI),
    path('login/', login)
]
'''

# PART D

'''
from .views import PersonAPI, login

urlpatterns = [
    path('person/', PersonAPI.as_view()),
    path('login/', login)
]
'''

# PART E

from .views import PersonViewSet
from rest_framework.routers import DefaultRouter # type : ignore

router = DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls))
]