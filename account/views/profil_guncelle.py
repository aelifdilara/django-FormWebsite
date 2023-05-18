from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import ProfilDuzenlemeForm
from blog.models import SunCalisanModel, İdariCalisanModel


@login_required(login_url='/')
def profil_guncelle(request):
    if request.method == "POST":
        form = ProfilDuzenlemeForm(request.POST, request.FILES, instance= request.user)
        old_email = request.user.email
        if form.is_valid():

            email = form.cleaned_data['email']

            if SunCalisanModel.objects.filter(email=old_email).exists():

                user = SunCalisanModel.objects.get(email=old_email)
                user.email = email
                user.save()

            elif İdariCalisanModel.objects.filter(email=old_email).exists():
                
                user = İdariCalisanModel.objects.get(email=old_email)
                user.email = email
                user.save()

            form.save()
            messages.success(request, 'Profil güncellendi.')

    else:
        form = ProfilDuzenlemeForm(instance = request.user)

    return render(request, 'pages/profil-guncelle.html', context={'form': form})