from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, SignInForm
from .models import MyUser

# Create your views here.


@login_required
def index(request):
    html = 'index.html'
    User = settings.AUTH_USER_MODEL
    context = {'User': User}
    return render(request, html, context)


def signupview(request):
    html = 'signup.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser.objects.create_user(
                display_name=data['display_name'],
                username=data['username'],
                password=data['password'],
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = SignUpForm()
    context = {'form': form}
    return render(request, html, context)


def signinview(request):
    html = 'signin.html'
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))

    form = SignInForm()
    context = {'form': form}
    return render(request, html, context)


def signoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('signin'))