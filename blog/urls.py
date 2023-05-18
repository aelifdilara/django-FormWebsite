from django.urls import path
from blog.views import liste, profil, sarf_malzeme_form, hijyen_form, tasima_form, rapor, detay, detay_tasima, detay_sarf
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from blog.views.giris import CustomLoginView
from . import views
urlpatterns = [


    path('giris/', CustomLoginView.as_view(template_name='pages/giris.html'), name='giris'),
    path('liste',liste, name='liste'),
    path('form',sarf_malzeme_form, name='sarf_malzeme_form'),
    path('profil',profil, name='profil'),
    path('', CustomLoginView.as_view(template_name='pages/giris.html'), name='giris'),
    path('sarfmalzemeformu', sarf_malzeme_form, name='sarf_malzeme_form'),
    path('hijyenformu', hijyen_form, name='hijyen_form'),
    path('tasimaformu', tasima_form, name='tasima_form'),
    path('rapor', rapor, name='rapor'),
    path('detay/<slug:detaySlug>', detay, name='detay'),
    path('detay_sarf/<slug:detaySlug>', detay_sarf, name='detay_sarf'),
    path('detay_tasima/<slug:detaySlug>', detay_tasima, name='detay_tasima')
]