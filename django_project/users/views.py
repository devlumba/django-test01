from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account {username} was successfully created")
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, template_name='users/register.html', context={'form': form})
