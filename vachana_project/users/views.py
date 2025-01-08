# from django.shortcuts import render

# # Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# from vachana_project.vachana_project.settings import LOGIN_REDIRECT_URL
from django.conf import settings

from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})



def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin:index')  # Redirect to admin page if superuser
                else:
                    return redirect(settings.LOGIN_REDIRECT_URL)  # Redirect to home page for regular user
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Invalid form data.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

from .forms import CustomUserUpdateForm  # You'll need to create a form for updating user details


# from collections import Counter

@login_required
def profile(request):
   
    return render(request, 'users/profile.html')


def profile_update(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomUserUpdateForm(instance=request.user)
    # Pass form errors to the template
    form_errors = form.errors.as_data()
    return render(request, 'users/profile_update.html', {'form': form,'form_errors': form_errors})
