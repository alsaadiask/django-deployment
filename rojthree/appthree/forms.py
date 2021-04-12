from django import forms
from appthree.models import userinfo

class NewUserForm(forms.ModelForm):
    class Meta:
        model = userinfo
        fields = '__all__'