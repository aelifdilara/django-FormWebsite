from django.shortcuts import render, get_object_or_404
from blog.models.sarf_malzeme_formu import SarfMalzemeModel

def detay_sarf(request, detaySlug):
    yazi = get_object_or_404(SarfMalzemeModel, slug=detaySlug)

    return render(request, 'pages/detay.html', context={
        'yazi': yazi,
    })