from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm
from .models import User

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('customer_list')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})