from rest_framework.decorators import api_view #type: ignore
from rest_framework.response import Response #type: ignore

# Create your views here.

# PART A

'''
@api_view(['GET'])
def index(request):
    course_name = 'Python Frameworks for the Web'
    course_contents = ['Flask', 'Django', 'Tornado']
    provider = 'ABC University'
    certificate = True
    live = True
    mode = 'Online'
    courses = {
        'course_name' : course_name,
        'course_contents': course_contents,
        'provider': provider,
        'certificate': certificate,
        'live': live,
        'mode': mode
    }
    return Response(courses)
'''

# PART B

'''
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def index(request):
    if request.method == 'GET':
        request_method = 'GET'
    elif request.method == 'POST':
        request_method = 'POST'
    elif request.method == 'PUT':
        request_method = 'PUT'
    elif request.method == 'PATCH':
        request_method = 'PATCH'
    elif request.method == 'DELETE':
        request_method = 'DELETE'
    course_name = 'Python Frameworks for the Web'
    course_contents = ['Flask', 'Django', 'Tornado']
    provider = 'ABC University'
    certificate = True
    live = True
    mode = 'Online'
    courses = {
        'course_name' : course_name,
        'course_contents': course_contents,
        'provider': provider,
        'certificate': certificate,
        'live': live,
        'mode': mode,
        'request_method': request_method
    }
    return Response(courses)
'''

# PART C

'''
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def index(request):
    if request.method == 'GET':
        request_method = 'GET'
    elif request.method == 'POST':
        data = request.data
        print('------------FETCHING RECEIVED DATA------------')
        print(data)
        print('----------------------------------------------')
        request_method = 'POST'
    elif request.method == 'PUT':
        request_method = 'PUT'
    elif request.method == 'PATCH':
        request_method = 'PATCH'
    elif request.method == 'DELETE':
        request_method = 'DELETE'
    course_name = 'Python Frameworks for the Web'
    course_contents = ['Flask', 'Django', 'Tornado']
    provider = 'ABC University'
    certificate = True
    live = True
    mode = 'Online'
    courses = {
        'course_name' : course_name,
        'course_contents': course_contents,
        'provider': provider,
        'certificate': certificate,
        'live': live,
        'mode': mode,
        'request_method': request_method
    }
    return Response(courses)
'''

# PART D

'''
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def index(request):
    if request.method == 'GET':
        print('------------FETCHING RECEIVED DATA------------')
        print(request.GET.get('search'))
        print('----------------------------------------------')
        request_method = 'GET'
    elif request.method == 'POST':
        request_method = 'POST'
    elif request.method == 'PUT':
        request_method = 'PUT'
    elif request.method == 'PATCH':
        request_method = 'PATCH'
    elif request.method == 'DELETE':
        request_method = 'DELETE'
    course_name = 'Python Frameworks for the Web'
    course_contents = ['Flask', 'Django', 'Tornado']
    provider = 'ABC University'
    certificate = True
    live = True
    mode = 'Online'
    courses = {
        'course_name' : course_name,
        'course_contents': course_contents,
        'provider': provider,
        'certificate': certificate,
        'live': live,
        'mode': mode,
        'request_method': request_method
    }
    return Response(courses)
'''

# PART E

'''
from .models import Person
from .serializers import PersonSerializer

@api_view(['GET', 'POST'])
def PersonAPI(request):
    if request.method == 'GET':
        objects = Person.objects.all()
        serializer = PersonSerializer(objects, many=True)
        return Response(serializer.data)
    else:
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
'''

# PART F

'''
from .models import Person
from .serializers import PersonSerializer

@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def PersonAPI(request):
    if request.method == 'GET':
        objects = Person.objects.all()
        serializer = PersonSerializer(objects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        object = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(object, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
'''

# PART G

'''
from .models import Person
from .serializers import PersonSerializer

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def PersonAPI(request):
    if request.method == 'GET':
        objects = Person.objects.all()
        serializer = PersonSerializer(objects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        object = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(object, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        object = Person.objects.get(id = data['id'])
        object.delete()
        return Response({'message': 'Person Details Removed'})
'''

# PART H

'''
from .models import Person
from .serializers import PersonSerializer

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def PersonAPI(request):
    if request.method == 'GET':
        objects = Person.objects.filter(course__isnull = False)
        serializer = PersonSerializer(objects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        object = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(object, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        object = Person.objects.get(id = data['id'])
        object.delete()
        return Response({'message': 'Person Details Removed'})
'''

# PART I

'''
from .models import Person
from .serializers import PersonSerializer, LoginSerializer

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data = data)
    if serializer.is_valid():
        data = serializer.validated_data
        return Response({'message': 'Logged In'})
    return Response(serializer.errors)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def PersonAPI(request):
    if request.method == 'GET':
        objects = Person.objects.filter(course__isnull = False)
        serializer = PersonSerializer(objects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        object = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(object, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        object = Person.objects.get(id = data['id'])
        object.delete()
        return Response({'message': 'Person Details Removed'})
'''

# PART J

'''
from .models import Person
from .serializers import PersonSerializer, LoginSerializer
from rest_framework.views import APIView #type: ignore

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data = data)
    if serializer.is_valid():
        data = serializer.validated_data
        return Response({'message': 'Logged In'})
    return Response(serializer.errors)

class PersonAPI(APIView):
    def get(self, request):
        objects = Person.objects.filter(course__isnull = False)
        serializer = PersonSerializer(objects, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def put(self, request):
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def patch(self, request):
        data = request.data
        object = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(object, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request):
        data = request.data
        object = Person.objects.get(id = data['id'])
        object.delete()
        return Response({'message': 'Person Details Removed'})
'''

# PART K

from rest_framework import viewsets # type: ignore
from .serializers import PersonSerializer
from .models import Person

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()