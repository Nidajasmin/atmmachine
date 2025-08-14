# api/serializers.py
from rest_framework import serializers
from .models import BankUser

class BankUserSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    masked_card_number = serializers.SerializerMethodField()
    dob = serializers.SerializerMethodField()
    join_date = serializers.SerializerMethodField()
    contact_number = serializers.SerializerMethodField()  # normalized name

    class Meta:
        model = BankUser
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'account_number',
            'ifsc',
            'balance',
            'contact_number',
            'image_url',
            'dob',
            'join_date',
            'masked_card_number',
            'branch',
            'aadhaar_number',
        ]

    def get_image_url(self, obj):
        request = self.context.get('request')
        img = getattr(obj, 'photo', None)
        if img:
            if request:
                return request.build_absolute_uri(img.url)
            return img.url
        return None

    def get_masked_card_number(self, obj):
        card = getattr(obj, 'card_number', '') or ''
        digits = ''.join(ch for ch in str(card) if ch.isdigit())
        if len(digits) >= 4:
            return '**** **** **** ' + digits[-4:]
        return None

    def _format_date(self, val):
        if not val:
            return None
        try:
            return val.strftime('%Y-%m-%d')
        except:
            return str(val)

    def get_dob(self, obj):
        return self._format_date(getattr(obj, 'dob', None))

    def get_join_date(self, obj):
        # your model uses 'date' as join date
        return self._format_date(getattr(obj, 'date', None))

    def get_contact_number(self, obj):
        # model field name is Contact_number (capital C) — normalize here
        return getattr(obj, 'Contact_number', None)
