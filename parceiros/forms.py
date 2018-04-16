from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django import forms
from django.contrib.auth.models import User
from parceiros.models import *
from django.core.validators import RegexValidator, URLValidator
from django.core.validators import ValidationError
from django.conf import settings


def validate_email(value):
    if User.objects.filter(email=value):
        raise ValidationError(
            _('%s já existe.' % (value))
        )

class UserForm(forms.ModelForm):
    email = forms.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = ('email',)