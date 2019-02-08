from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cliente/', views.cliente_list),
    path('cliente/<int:cliente_id>/', views.cliente_show),
    path('medico/', views.medico_list),
    path('medico/<int:medico_id>/', views.medico_show),
    path('cliente/form/', views.cliente_form),
    path('medico/form/', views.medico_form)
]