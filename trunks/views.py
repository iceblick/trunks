from django.shortcuts import render
from django.utils import timezone
from .models import Trunk_OTN
from .models import Trunk_DWDM
from .models import Trunk_SDH

# Create your views here.

def trunk_list(request):
    otn = Trunk_OTN.objects.filter(Published_date__lte=timezone.now()).order_by('Published_date')
    dwdm = Trunk_DWDM.objects.filter(Published_date__lte=timezone.now()).order_by('Published_date')
    sdh = Trunk_SDH.objects.filter(Published_date__lte=timezone.now()).order_by('Published_date')
    return render(request, 'trunks/trunk_list.html', {'otn': otn, 'dwdm': dwdm, 'sdh': sdh})