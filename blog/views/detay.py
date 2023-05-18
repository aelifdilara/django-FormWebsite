from django.shortcuts import render, get_object_or_404
from blog.models.hijyen_formu import HijyenModel
from blog.models.tasima_formu import TasimaModel
from blog.models.sarf_malzeme_formu import SarfMalzemeModel

def detay(request, detaySlug):
    yazi = get_object_or_404(HijyenModel, slug=detaySlug)

    return render(request, 'pages/detay.html', context={
        'yazi': yazi,
    })