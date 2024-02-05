from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# from .models import Profile


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


@login_required
def logout_page(request):
    return render(request, template_name='users/logout-page.html', context={"title": "Logout"})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)
