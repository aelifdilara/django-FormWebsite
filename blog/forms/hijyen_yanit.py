from django import forms
from blog.models import HijyenYanitModel

class HijyenYanit(forms.ModelForm):

    class Meta:
        model = HijyenYanitModel
        fields = ( 
            'aciklama', 'gorevli_isim_soyisim'
        )