from django.forms import ModelForm
from .models import *


class my_form(ModelForm):
    class Meta:
        model = file_and_pic
        fields = '__all__'
