from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import requests
import json

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        captcha_token = request.POST.get("g-recaptcha-response")
        cap_url = "https://www.google.com/recaptcha/api/siteverify"
        cap_secret = "6LeDcoYaAAAAACgrY1SN-GuVF_jCZAnizneyUenh"
        cap_data = {"secret": cap_secret, "response": captcha_token}
        cap_server_response = requests.post(url=cap_url, data=cap_data)
        cap_json = json.loads(cap_server_response.text)
        if cap_json['success'] == False:
            messages.success(request, "Invalid ReCaptcha")
            return render(request, 'users/register.html', {'form': form})
        if (form.is_valid() and cap_json['success'] == True):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

"""
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
            print("[System] User: " + username + " : invalid ReCaptcha")
            return render(request, self.template, {'form': form})
        if user is not None:
            login(request, user)
            print("[System] User: " + username + " : was loggined")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Invalid Login data")
            print("[System] Access denied : invalid login data")
            return render(request, self.template, {'form': form})
"""


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
