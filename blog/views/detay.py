from django.shortcuts import render, get_object_or_404, redirect
from blog.models.hijyen_formu import HijyenModel
from blog.models.tasima_formu import TasimaModel
from blog.models.sarf_malzeme_formu import SarfMalzemeModel
from blog.models.malzeme import MalzemeModel


def detay(request, Formslug, slug):
    model_map = {
        'hijyen': HijyenModel,
        'tasima': TasimaModel,
        'sarf-malzeme': SarfMalzemeModel,
    }

    Model = model_map.get(Formslug)

    form = get_object_or_404(Model, slug=slug)
    #malzemeler = SarfMalzemeModel.objects.values_list('sarf_malzeme_adi__malzeme_adi', flat=True)
    malzemeler = MalzemeModel.objects.values_list('malzeme_adi', flat=True).distinct()


    if request.method == 'POST':
        if 'guncelle' in request.POST:
            aciklama = request.POST.get('aciklama')
            form.aciklama  = aciklama
            if(Formslug == "sarf-malzeme"):

                sarf_malzeme_adi = request.POST.get('sarf_malzeme_adi')
                sarf_malzeme_adedi = request.POST.get('sarf_malzeme_adedi')
                malzeme = MalzemeModel.objects.get(malzeme_adi=sarf_malzeme_adi)
                form.sarf_malzeme_adi  = malzeme
                form.sarf_malzeme_adedi  = sarf_malzeme_adedi

            form.save()

        elif 'sil' in request.POST:
            form.delete()
            return redirect('liste')



    return render(request, 'pages/detay.html', context={
        'form': form,
        'malzemeler': malzemeler

    })