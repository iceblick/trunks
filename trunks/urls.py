from django.urls import path
from . import views

urlpatterns = [
	path('', views.trunk_list, name='trunk_list'),
]