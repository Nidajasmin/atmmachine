from django.shortcuts import render, redirect
from .forms import BankUserForm
from .models import BankUser
from django.contrib import messages


def dashboard(request):
    return render(request, 'dashboard.html')


def register_user(request):
    if request.method == 'POST':
        form = BankUserForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully!")
            return redirect('user_list')
    else:
        form = BankUserForm()
    return render(request, 'register.html', {'form': form})



def user_list(request):
    users = BankUser.objects.all().order_by('-id') 
    return render(request, 'user_list.html', {'users': users})

def edit_user(request, user_id):
    user = BankUser.objects.get(id=user_id)
    if request.method == 'POST':
        form = BankUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User details updated successfully!")
            return redirect('user_list')
    else:
        form = BankUserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form, 'user': user})

def atm_interface(request):
    return render(request, 'atm_interface.html')

