# from django import forms
# from .models import BankUser
# from django.core.validators import RegexValidator


# class BankUserForm(forms.ModelForm):
#     confirm_pin = forms.CharField(
#         max_length=6,
#         widget=forms.PasswordInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Confirm your PIN'
#         }),
#         label='Confirm PIN',
#         required=True
#     )

#     # ✅ Add this dummy field to trick autofill
#     x_last_name = forms.CharField(
#         required=False,
#         label='Last name',  # Keeps label same
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter your last name',
#             'autocomplete': 'off',
#             'id': 'id_x_last_name'
#         })
#     )

#     class Meta:
#         model = BankUser
#         fields = [
#             'date', 'first_name', 'dob', 'aadhaar_number',
#             'account_number', 'branch', 'ifsc', 'Contact_number',
#             'email', 'card_number', 'card_pin', 'photo', 'balance',
#             'last_name'  # Keep last_name in fields list
#         ]

#         widgets = {
#             'last_name': forms.HiddenInput(),  # hide actual last_name
#             'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'readonly': True}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
#             'card_number': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
#             'card_pin': forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
#             'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#             'account_number': forms.TextInput(attrs={'class': 'form-control'}),
#             'branch': forms.TextInput(attrs={'class': 'form-control'}),
#             'ifsc': forms.TextInput(attrs={'class': 'form-control'}),
#             'Contact_number': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
#             'balance': forms.NumberInput(attrs={'class': 'form-control'}),
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         # ✅ Copy dummy field value into the real field
#         cleaned_data['last_name'] = self.data.get('x_last_name', '').strip()

#         pin = cleaned_data.get("card_pin")
#         confirm_pin = cleaned_data.get("confirm_pin")
#         if pin and confirm_pin and pin != confirm_pin:
#             self.add_error('confirm_pin', "PINs do not match.")

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # Optional: format Aadhaar nicely
#         aadhaar = self.initial.get('aadhaar_number')
#         if aadhaar and len(aadhaar) == 12 and aadhaar.isdigit():
#             self.initial['aadhaar_number'] = f"{aadhaar[:4]} {aadhaar[4:8]} {aadhaar[8:]}"


#     def clean_card_pin(self):
#         pin = self.cleaned_data.get('card_pin', '')
#         if not pin.isdigit():
#             raise forms.ValidationError("PIN must be numeric.")
#         if len(pin) < 4 or len(pin) > 6:
#             raise forms.ValidationError("PIN must be 4 to 6 digits long.")
#         return pin

#     def clean_Contact_number(self):
#         phone = self.cleaned_data.get('Contact_number', '').strip().replace(' ', '')
#         if not phone.startswith('+') or not phone[1:].isdigit():
#             raise forms.ValidationError("Enter a valid international mobile number.")
#         return phone

#     def clean_aadhaar_number(self):
#         aadhaar = self.cleaned_data.get('aadhaar_number', '')
#         aadhaar = aadhaar.replace(' ', '')
#         if len(aadhaar) != 12 or not aadhaar.isdigit():
#             raise forms.ValidationError("Enter a valid 12-digit Aadhaar number.")
#         return aadhaar

    

from django import forms
from .models import BankUser


class BankUserForm(forms.ModelForm):
    aadhaar_number = forms.CharField(
        max_length=19,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'XXXX XXXX XXXX',
            'inputmode': 'numeric',
            'autocomplete': 'off',
            'maxlength': '19'
        })
    )

    confirm_pin = forms.CharField(
        max_length=6,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your PIN',
            'autocomplete': 'new-password'
        }),
        label='Confirm PIN',
        required=True
    )

    class Meta:
        model = BankUser
        fields = [
            'date', 'first_name', 'last_name', 'dob', 'aadhaar_number',
            'account_number', 'branch', 'ifsc', 'Contact_number',
            'email', 'card_number', 'card_pin', 'photo', 'balance'
        ]

        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date', 'readonly': True, 'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter your first name',
                'autocomplete':"off"
            }),
            'last_name': forms.TextInput(attrs={
            'class': 'form-control',
             'placeholder': 'Enter your last name',
             'autocomplete': 'off-last-name'
            }),
           
            'dob': forms.DateInput(attrs={
                'type': 'date', 'class': 'form-control'
            }),
            'account_number': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter 12 digit account number',
                'autocomplete':"off"
            }),
            'branch': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter branch name',
                'autocomplete':"off"
            }),
            'ifsc': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter IFSC code',
                'autocomplete':"off"
            }),
            'Contact_number': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'e.g. +919876543210',
                'autocomplete':"off"
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'name@example.com',
                'autocomplete':"off"
            }),
            
            'card_number': forms.TextInput(attrs={
             'class': 'form-control',
            'placeholder': 'Enter 16-digit card number',
            'autocomplete': 'off-card-number'
            }),
            'card_pin': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': '4 to 6 digit PIN',
                'autocomplete': 'new-password'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'balance': forms.NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter initial balance'
            }),
        }

    def clean_card_pin(self):
        pin = self.cleaned_data.get('card_pin', '')
        if not pin.isdigit():
            raise forms.ValidationError("PIN must be numeric.")
        if len(pin) < 4 or len(pin) > 6:
            raise forms.ValidationError("PIN must be 4 to 6 digits long.")
        return pin

    def clean_Contact_number(self):
        phone = self.cleaned_data.get('Contact_number', '').strip().replace(' ', '')
        if not phone.startswith('+') or not phone[1:].isdigit():
            raise forms.ValidationError("Enter a valid international mobile number.")
        return phone

    def clean_aadhaar_number(self):
        aadhaar = self.cleaned_data.get('aadhaar_number', '')
        aadhaar = aadhaar.replace(' ', '')
        if len(aadhaar) != 12 or not aadhaar.isdigit():
            raise forms.ValidationError("Enter a valid 12-digit Aadhaar number.")
        return aadhaar

    def clean(self):
        cleaned_data = super().clean()
        pin = cleaned_data.get("card_pin")
        confirm_pin = cleaned_data.get("confirm_pin")
        if pin and confirm_pin and pin != confirm_pin:
            self.add_error('confirm_pin', "PINs do not match.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Format Aadhaar on load
        aadhaar = self.initial.get('aadhaar_number')
        if aadhaar and len(aadhaar) == 12 and aadhaar.isdigit():
            self.initial['aadhaar_number'] = f"{aadhaar[:4]} {aadhaar[4:8]} {aadhaar[8:]}"


    


class InsertCardForm(forms.Form):
    card_number = forms.CharField(
        max_length=16,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter 16-digit Card Number'
        })
    )
    pin = forms.CharField(
        max_length=6,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter 4–6 digit PIN'
        })
    )


class TransactionForm(forms.Form):
    to_account = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter recipient account number'
        }),
        label='Recipient Account Number'
    )
    amount = forms.DecimalField(
        max_digits=10, decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter amount to transfer'
        }),
        label='Amount to Transfer'
    )
