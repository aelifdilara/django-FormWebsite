from django import forms
from blog.models import SarfMalzemeYanitModel

class SarfYanit(forms.ModelForm):

    class Meta:
        model = SarfMalzemeYanitModel
        fields = ( 
            'aciklama',
        )