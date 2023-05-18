from django.shortcuts import render, get_object_or_404
from blog.models.tasima_formu import TasimaModel

def detay_tasima(request, detaySlug):
    yazi = get_object_or_404(TasimaModel, slug=detaySlug)

    return render(request, 'pages/detay.html', context={
        'yazi': yazi,
    })