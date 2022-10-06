from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import Http404

from .forms import OwnerForm, VehicleForm
from .models import Owner, Vehicle

# Create your views here.

def index(request):
    Owners = Owner.objects.all()

    context = {'Owners': Owners}
    return render(request, 'vehicle/index.html', context)

def createOwner(request):
    Owners = Owner.objects.all()
    form = OwnerForm()

    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'Owners': Owners, 'form': form}
    return render(request, 'vehicle/create_owner.html', context)

def createVehicle(request):
    Vehicles = Vehicle.objects.all()
    form = VehicleForm()

    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('owner_vehicle/<str:pk>')
    
    context = {'Vehicles': Vehicles, 'form': form}
    return render(request, 'vehicle/create_vehicle.html', context)

def ownerVehicle(request, pk):
    owner = Owner.objects.get(id=pk)
    Vehicles = Vehicle.objects.all()
    
    context = {'owner':owner, 'Vehicles': Vehicles}

    return render(request, 'vehicle/owner_vehicle.html', context)