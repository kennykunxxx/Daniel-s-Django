from django.shortcuts import render, redirect
from .forms import loginform, UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

def LogginIn(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('movie:dashboard')
                else:
                    return HttpResponse('Disabled Account')
            else:
                HttpResponse('Account does not exist')
    else:
        form = loginform()
    return render(request, 'login/login.html', {'form': form}) 
    
def CreateUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(new_user.cleaned_data['passsword'])
            new_user.save()
            return render(request, 'login/register_complete.html', {'new_user': new_user})
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})
# Create your views here.
