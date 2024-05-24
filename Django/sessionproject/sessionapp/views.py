from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse('<h1>Django<br>The session is set</h1>')

def access_session(request):
    response = "<h1>Welcome to Sessions of Django</h1>"
    if request.session.get('name'):
        response += "Name: {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password: {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create_session')