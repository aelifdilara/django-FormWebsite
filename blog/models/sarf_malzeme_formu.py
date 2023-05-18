from django.db import models
from blog.models.malzeme import MalzemeModel
from autoslug import AutoSlugField
from blog.abstract_models import TalepFormuAbstractModel
from blog.models.kategori import KategoriModel

class SarfMalzemeModel(TalepFormuAbstractModel):
    sarf_malzeme_adi = models.ForeignKey(MalzemeModel, on_delete=models.CASCADE,related_name='sarf_malzeme_ismi')
    sarf_malzeme_adedi = models.IntegerField()
    kategori_ismi = models.ForeignKey(KategoriModel,on_delete=models.CASCADE,related_name='kategori_ismi')
    #form_kategori = models.ForeignKey(FormKategoriModel, related_name='sarf_malzeme_kategorileri', on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from = 'baslik', unique=True, null = True, blank=True, allow_unicode=True)

    class Meta:
        db_table = 'sarf_malzeme'
        verbose_name_plural = 'Sarf Malzeme Formları'
        verbose_name = 'Sarf Malzeme Formu'

    def __str__(self): #admin panelinde isim olarak görünmesi için
        return self.baslik