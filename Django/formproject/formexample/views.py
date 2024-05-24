from django.shortcuts import render
from .forms import ExampleForm
from django.http import HttpResponse
# Create your views here.
def view_function(request):
    form = ExampleForm()
    return render(request, "formexample/template.html", {
        "form": form
    })

def valid_function(request):
    if request.method == "POST":
        # if the submit button has been pressed
        form = ExampleForm(request.POST or None)
        if form.is_valid():
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            rollno = form.cleaned_data.get('roll_number')
            return HttpResponse(f'First Name: {fname}, Last Name: {lname}, Roll Number: {rollno}')
    else:
        # if the submit button has not been pressed, i.e., the page has just loaded and waiting for user input
        form = ExampleForm()
    return render(request, "formexample/template.html", {
        "form": form
    })