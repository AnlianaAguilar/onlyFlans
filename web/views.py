from django.shortcuts import render, redirect
from .models import Flan
from .forms import ContactFormForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
def index(request):
  flanes_publicos= Flan.objects.filter(is_private=False)
  return render(request, 'index.html', {'flanes': flanes_publicos})


def about(request):
  return render(request, 'about.html')


def error_404(request):
    return render(request, '404.html', status=404)




@login_required
def welcome(request):
  flanes_privados = Flan.objects.filter(is_private=True)
  return render(request, 'welcome.html', {'flanes': flanes_privados})


def contacto(request):
  if request.method == 'POST':
    form = ContactFormForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('exito') 
  else:
    form = ContactFormForm()
   
  return render(request, 'contacto.html', {'form':form})

def exito(request):
  return render(request, 'exito.html')

def flan_detail(request, flan_id):
  flan = Flan.objects.get(id=flan_id)
  return render(request, 'flan_detail.html', {'flan': flan})

class CustomLoginView(LoginView):
  template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
  next_page = '/'
