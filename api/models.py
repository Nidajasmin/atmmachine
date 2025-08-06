from django.db import models
from django.core.validators import (
    RegexValidator, MinLengthValidator, MaxLengthValidator, EmailValidator
    
)
from datetime import date

class BankUser(models.Model):
    date = models.DateField(default=date.today)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    account_number = models.CharField(
        max_length=12,
        unique=True,
        validators=[RegexValidator(r'^\d{10,12}$', 'Account number must be 12 digits')]
    )
    branch = models.CharField(max_length=50)
    ifsc = models.CharField(
        max_length=11,
        validators=[RegexValidator(
            r'^[A-Z]{4}0[A-Z0-9]{6}$',
            'Invalid IFSC. Format: 4 letters, 0, then 6 alphanumerics (e.g., SBIN0001234)'
        )]
    )
    aadhaar_number = models.CharField(
        max_length=12,
        validators=[RegexValidator(r'^\d{12}$', 'Aadhaar must be a 12-digit number')]
    )
    Contact_number = models.CharField(
        max_length=13,
        validators=[RegexValidator(r'^\+91\d{10}$', 'Mobile must be +91 followed by 10 digits')]
    )
    email = models.EmailField(validators=[EmailValidator('Enter a valid email address')])
    card_number = models.CharField(
        max_length=16,
        validators=[RegexValidator(r'^\d{16}$', 'Card number must be exactly 16 digits')]
    )
    card_pin = models.CharField(
        max_length=6,
        validators=[
            RegexValidator(r'^\d+$', 'PIN must be numeric only'),
            MinLengthValidator(4, message="PIN must be at least 4 digits"),
            MaxLengthValidator(6, message="PIN can be at most 6 digits"),
        ]
    )
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    
    # ✅ Newly added field
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    pin = models.CharField(max_length=6,default='0000')


    class Meta:
        db_table = 'bankuser'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'bankuser'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

   




