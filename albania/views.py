from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import City, Attraction, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('albania')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User dose not exist!!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'Username or password dose not exist')

    context = {'page': page}
    return render(request, 'albania/login_register.html', context)


def logout_user(request):
    logout(request)
    return redirect('albania')



def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('albania')
        else:
            messages.error(request, 'An error occurred registration ')

    return render(request, 'albania/login_register.html', {'form': form})

def index(request):
    return render(request, 'albania/index.html')


def home(request):
    return render(request, 'albania/albania.html')


@login_required(login_url='albania')
def city(request):
    city = City.objects.all()
    context = {'city': city}
    return render(request, 'albania/city.html', context)


@login_required(login_url='albania')
def attraction(request):
    attraction = Attraction.objects.all()
    context = {"attraction": attraction}
    return render(request, 'albania/attraction.html', context)


@login_required(login_url='albania')
def detail(request, id):
    cities = get_object_or_404(City, pk=id)
    return render(request, 'albania/citi_detail.html', {'cities': cities})


@login_required(login_url='albania')
def attraction_detail(request, id):
    attraction = get_object_or_404(Attraction, pk=id)
    return render(request, 'albania/attraction_detail.html', {"attraction": attraction})