from django import forms
from basicapp.models import User


class FormsName(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


