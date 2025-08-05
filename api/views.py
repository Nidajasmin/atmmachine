from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from decimal import Decimal
from .forms import BankUserForm, ATMAuthForm, TransactionForm
from .models import BankUser


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
    user = get_object_or_404(BankUser, id=user_id)
    if request.method == 'POST':
        form = BankUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User details updated successfully!")
            return redirect('user_list')
    else:
        form = BankUserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form, 'user': user})




def delete_user(request, user_id):
    user = get_object_or_404(BankUser, id=user_id)
    user.delete()
    messages.success(request, "User deleted successfully.")
    return redirect('user_list')





#authentication
def insert_card(request):
    if request.method == 'POST':
        form = ATMAuthForm(request.POST)
        if form.is_valid():
            card_number = form.cleaned_data['card_number']
            try:
                user = BankUser.objects.get(card_number=card_number)
                request.session['user_id'] = user.id
                request.session.modified = True
                return redirect('atm_menu')
            except BankUser.DoesNotExist:
                form.add_error('card_number', 'Invalid card number')
    else:
        form = ATMAuthForm()

    return render(request, 'insert_card.html', {'form': form})


def user_profile(request, user_id):
    user = get_object_or_404(BankUser, id=user_id)
    return render(request, 'user_profile.html', {'user': user})


# atmmenu
def atm_menu(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('payment')
    return render(request, 'menu.html')


#balance
def check_balance(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('payment')
    user = get_object_or_404(BankUser, id=user_id)
    return render(request, 'balance.html', {'balance': user.balance})


#deposit
def deposit(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('payment')
    user = get_object_or_404(BankUser, id=user_id)

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            amount = Decimal(str(form.cleaned_data['amount']))
            user.balance += amount
            user.save()
            messages.success(request, f"₹{amount} deposited successfully.")
            return redirect('atm_menu')
    else:
        form = TransactionForm()

    return render(request, 'deposit.html', {'form': form})



#withdraw
def withdraw(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('payment')
    user = get_object_or_404(BankUser, id=user_id)

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            amount = Decimal(str(form.cleaned_data['amount']))
            if user.balance >= amount:
                user.balance -= amount
                user.save()
                messages.success(request, f"₹{amount} withdrawn successfully.")
                return redirect('atm_menu')
            else:
                messages.error(request, "❌ Insufficient balance.")
                return redirect('atm_menu')
    else:
        form = TransactionForm()

    return render(request, 'withdraw.html', {'form': form})



def thank_you(request):
    request.session.flush() 
    return render(request, 'thankyou.html')










