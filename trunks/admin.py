from django.contrib import admin
from .models import Trunk_OTN
from .models import Trunk_DWDM
from .models import Trunk_SDH

# Register your models here.
admin.site.register(Trunk_OTN)
admin.site.register(Trunk_DWDM)
admin.site.register(Trunk_SDH)