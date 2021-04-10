# Create views here.
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.views import View

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserForm
import requests
import json
from django.contrib import messages

from django.conf import settings
from django.core.files.storage import FileSystemStorage

class Index(LoginRequiredMixin, View):
    template = 'index.html'
    login_url = '/login/'

    def get(self, request):
        return render(request, self.template)

    def post(request):
        if request.method == 'POST':
            upload_file = request.FILES('document')
            print(upload_file.name)
            print(upload_file.size)
        return render(request, 'index.html')



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
        captcha_token = request.POST.get("g-recaptcha-response")
        cap_url="https://www.google.com/recaptcha/api/siteverify"
        cap_secret="6LeDcoYaAAAAACgrY1SN-GuVF_jCZAnizneyUenh"
        cap_data = {"secret": cap_secret, "response":captcha_token}
        cap_server_response=requests.post(url=cap_url, data=cap_data)
        cap_json=json.loads(cap_server_response.text)
        if cap_json['success']==False:
            messages.error(request, "Invalid ReCaptcha")
            return render(request, self.template, {'form': form})
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Invalid Login data")
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

def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/templates/index.html')

