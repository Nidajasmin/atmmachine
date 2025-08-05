from django import forms
from .models import BankUser

class BankUserForm(forms.ModelForm):
    class Meta:
        model = BankUser
        fields = '__all__'

        widgets = {
            'Date': forms.DateInput(attrs={
                'type': 'date', 'readonly': True, 'class': 'form-control',
                'placeholder': 'Auto-filled today'
            }),
            'First_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first name'
            }),
            'Last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name'
            }),
            'dob': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select your birthdate'
            }),
            'Account_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter 12-digit account number'
            }),
            'Branch': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter bank branch name'
            }),
            'IFSC': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter IFSC (e.g., SBIN0001234)'
            }),
            'Aadhaar_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter 12-digit Aadhaar number'
            }),
            'Contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '10-digit mobile number'
            }),
            'Email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. name@example.com'
            }),
            'Card_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter 16-digit card number'
            }),
            'Card_pin': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': '4 to 6 digit PIN'
            }),
            'Photo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }



    def clean_card_pin(self):
        pin = self.cleaned_data.get('card_pin', '')
        if not pin.isdigit():
            raise forms.ValidationError("PIN must be numeric.")
        if len(pin) < 4 or len(pin) > 6:
            raise forms.ValidationError("PIN must be 4 to 6 digits long.")
        return pin
    
    def clean_contact_number(self):
        phone = self.cleaned_data.get('contact_number', '').strip().replace(' ', '')
        if not phone.startswith('+') or not phone[1:].isdigit():
            raise forms.ValidationError("Enter a valid international mobile number.")
        return phone
    


class ATMAuthForm(forms.Form):
    card_number = forms.CharField(max_length=16, label="Card Number")
    card_pin = forms.CharField(widget=forms.PasswordInput(), max_length=6, label="ATM PIN")

    def clean(self):
        cleaned_data = super().clean()
        card_number = cleaned_data.get("card_number")
        card_pin = cleaned_data.get("card_pin")

        if not card_number or not card_pin:
            return

        try:
            user = BankUser.objects.get(card_number=card_number)
        except BankUser.DoesNotExist:
            self.add_error('card_number', 'Invalid card number')
            return

        if user.card_pin != card_pin:
            self.add_error('card_pin', 'Incorrect PIN')

class TransactionForm(forms.Form):
    amount = forms.FloatField(min_value=1, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter amount'
    }))


