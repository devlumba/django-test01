from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account {username} was successfully created! Now you can log in your account.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, template_name='users/register.html', context={'form': form})


def logout_page(request):
    return render(request, template_name='users/logout-page.html', context={"title": "Logout"})


@login_required
def profile(request):
    return render(request, 'users/profile.html')