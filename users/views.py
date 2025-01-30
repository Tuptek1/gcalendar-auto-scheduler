from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})

@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('users:profile')  # Redirect to the profile page
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'users/profile_edit.html', {'form': form})  

def register_view(request):

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('tasks:task_list')
    else:
        form = CustomUserCreationForm()


    return render(request, 'users/register.html', {'form' : form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('tasks:task_list')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form' : form})

@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    return render(request, 'users/logged_out.html')