from django.urls import path
from . import views

urlpatterns = [
	path('', views.trunk_list, name='trunk_list'),
	path('Trunk_OTN/<int:pk>/', views.Trunk_OTN_detail, name='Trunk_OTN_detail'),
	path('Trunk_DWDM/<int:pk>/', views.Trunk_DWDM_detail, name='Trunk_DWDM_detail'),
	path('Trunk_SDH/<int:pk>/', views.Trunk_SDH_detail, name='Trunk_SDH_detail'),
]