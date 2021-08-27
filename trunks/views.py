from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Trunk_OTN
from .models import Trunk_DWDM
from .models import Trunk_SDH


# Create your views here.

def trunk_list(request):
    otn = Trunk_OTN.objects.filter(Published_date__lte=timezone.now()).order_by('Published_date')
    dwdm = Trunk_DWDM.objects.filter(Published_date__lte=timezone.now()).order_by('Published_date')
    sdh = Trunk_SDH.objects.filter(Published_date__lte=timezone.now()).order_by('Published_date')
    return render(request, 'trunks/trunk_list.html', {'otn': otn, 'dwdm': dwdm, 'sdh': sdh})

def Trunk_OTN_detail(request, pk):
    otn = get_object_or_404(Trunk_OTN, pk=pk)
    return render(request, 'trunks/Trunk_OTN_detail.html', {'otn': otn})

def Trunk_DWDM_detail(request, pk):
    dwdm = get_object_or_404(Trunk_DWDM, pk=pk)
    return render(request, 'trunks/Trunk_DWDM_detail.html', {'dwdm': dwdm})

def Trunk_SDH_detail(request, pk):
    sdh = get_object_or_404(Trunk_SDH, pk=pk)
    return render(request, 'trunks/Trunk_SDH_detail.html', {'sdh': sdh})