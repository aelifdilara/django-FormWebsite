from django.db import models
from blog.models.malzeme import MalzemeModel
from autoslug import AutoSlugField
from blog.abstract_models import TalepFormuAbstractModel
from blog.models.gorevli import GorevliModel

class TasimaModel(TalepFormuAbstractModel):
    gorevli_kisi = models.ForeignKey(GorevliModel,on_delete=models.CASCADE,related_name='gorevli_kisi_tasima')
    #görevli kişi adı ve sayıyı birbirine bağlama işlemi gerekiyor.
    slug = AutoSlugField(populate_from = 'baslik', unique=True, null = True, blank=True, allow_unicode=True)

    class Meta:
        db_table = 'tasima'
        verbose_name_plural = 'Tasima Formları'
        verbose_name = 'Tasima Formu'

    def __str__(self): #admin panelinde isim olarak görünmesi için
        return self.gorevli_kisi.gorevli_isim_soyisim