# Create views here.
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.views import View

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserForm



class Index(LoginRequiredMixin, View):
    template = 'index.html'
    login_url = '/login/'

    def get(self, request):
        return render(request, self.template)


class Login(View):
    template = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {'form': form})


    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template, {'form': form})


class Password(View):
    template = 'password-reset.html'

    def get(self, request):
        return render(request, self.template)


class Register(View):
    template = 'register.html'

    def get(self, request):
        form = UserForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password2']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            return render(request, self.template, {'form': form})


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

    