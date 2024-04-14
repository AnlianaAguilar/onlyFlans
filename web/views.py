from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def welcome(request):
  return render(request, 'welcome.html')