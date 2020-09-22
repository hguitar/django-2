from django.forms import ModelForm
from .models import file_and_pic


class my_form(ModelForm):
    class Meta:
        model = file_and_pic
        fields = '__all__'
