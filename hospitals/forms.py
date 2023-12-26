from django import forms
from .models import Hospital

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the 'required' attribute of the phone_number field to False
        self.fields['phone_number'].required = False
        