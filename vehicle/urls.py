from django.urls import path

from . import views

app_name = 'vehicle'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_owner', views.createOwner, name='create_owner'),
    path('create_vehicle', views.createVehicle, name='create_vehicle'),
    path('owner_vehicle/<str:pk>', views.ownerVehicle, name='owner_vehicle'),
]