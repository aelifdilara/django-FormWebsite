from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseForbidden

@login_required
def rapor(request):

    if not request.user.is_staff:
        return HttpResponseForbidden("Bu sayfaya erişmek için yetkiniz yok.")  

    data = "Current Data"      

    context = {
        "data":data
    }
    
    return render(request, 'pages/rapor.html', context)