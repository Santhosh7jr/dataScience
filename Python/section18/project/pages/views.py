from django.shortcuts import render

from django.http import HttpResponse

def home(req):
  return HttpResponse("hello!")

def display_lists(request):
    fruits = ['Apple', 'Banana', 'Mango', 'Orange']
    students = ['Hemanth Kumara H Y', 'Anita', 'Kiran', 'Sneha']

    return render(request, 'pages/index.html', {
        'fruits': fruits,   
        'students': students
    })