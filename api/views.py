from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from decimal import Decimal
from .forms import BankUserForm,InsertCardForm,TransactionForm 
from .models import BankUser


def dashboard(request):
    return render(request, 'dashboard.html')


def register_user(request):
    if request.method == 'POST':
        form = BankUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            storage = messages.get_messages(request)
            for _ in storage:
                pass  
            messages.success(request, "User registered successfully!")
            return redirect('user_list')
        else:
            messages.error(request, "Please correct the errors below.")
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


# authentication
def insert_card(request):
    if request.method == 'POST':
        form = InsertCardForm(request.POST)
        if form.is_valid():
            card_number = form.cleaned_data['card_number']
            pin = form.cleaned_data['pin']

            try:
                user = BankUser.objects.get(card_number=card_number)
                if user.card_pin == pin:
                    request.session['user_id'] = user.id
                    return redirect('atm_menu')
                else:
                    messages.error(request, "❌ Incorrect PIN.")
            except BankUser.DoesNotExist:
                messages.error(request, "❌ Invalid card number.")
    else:
        form = InsertCardForm()

    return render(request, 'insert_card.html', {'form': form})


def user_profile(request, user_id):
    user = get_object_or_404(BankUser, id=user_id)
    return render(request, 'user_profile.html', {'user': user})


def atm_menu(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('payment')
    return render(request, 'menu.html')


def check_balance(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('payment')
    user = get_object_or_404(BankUser, id=user_id)
    return render(request, 'balance.html', {'balance': user.balance})


def deposit(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('payment')
    user = get_object_or_404(BankUser, id=user_id)

    if request.method == 'POST':
        amount = request.POST.get('amount')
        try:
            amount = Decimal(amount)
            if amount > 0:
                user.balance += amount
                user.save()
                messages.success(request, f"₹{amount} deposited successfully.")
                return redirect('atm_menu')
            else:
                messages.error(request, "Enter a valid amount.")
        except:
            messages.error(request, "Invalid amount entered.")
    return render(request, 'deposit.html')


def withdraw(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('payment')
    user = get_object_or_404(BankUser, id=user_id)

    if request.method == 'POST':
        amount = request.POST.get('amount')
        try:
            amount = Decimal(amount)
            if amount <= 0:
                messages.error(request, "Amount must be greater than zero.")
            elif user.balance >= amount:
                user.balance -= amount
                user.save()
                messages.success(request, f"₹{amount} withdrawn successfully.")
                return redirect('atm_menu')
            else:
                messages.error(request, "❌ Insufficient balance.")
        except:
            messages.error(request, "Invalid amount entered.")
    return render(request, 'withdraw.html')





def transaction(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('payment')

    user = get_object_or_404(BankUser, id=user_id)

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            to_account = form.cleaned_data['to_account']
            amount = form.cleaned_data['amount']

            if amount <= 0:
                messages.error(request, "Amount must be greater than 0.")
                return redirect('transaction')

            if user.account_number == to_account:
                messages.error(request, "Cannot transfer to your own account.")
                return redirect('transaction')

            try:
                recipient = BankUser.objects.get(account_number=to_account)
            except BankUser.DoesNotExist:
                messages.error(request, "Recipient account not found.")
                return redirect('transaction')

            if user.balance >= amount:
                user.balance -= amount
                recipient.balance += amount
                user.save()
                recipient.save()
                messages.success(request, f"₹{amount} transferred to account {to_account} successfully.")
                return redirect('atm_menu')
            else:
                messages.error(request, "Insufficient balance.")
    else:
        form = TransactionForm()

    return render(request, 'transaction.html', {'form': form})


def thank_you(request):
    request.session.flush()
    return render(request, 'thankyou.html')

