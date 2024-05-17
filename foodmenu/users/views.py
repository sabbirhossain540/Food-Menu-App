from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
import sys

# Create your views here.
def register(request):
    
    if request.method == 'POST':
        
        form = RegisterForm(request.POST)
        # if not form.is_valid():
        #     print(form.errors)
        #     breakpoint()
        if form.is_valid():  # Ensure form is valid before accessing cleaned_data
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Replace 'some-view-name' with your desired redirect target
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
