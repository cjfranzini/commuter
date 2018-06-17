from django.shortcuts import render
from subway.models import Trip

# Create your views here.
def index(request):
    trip_list = Trip.objects.order_by('-date')[:10]
    context = {'trip_list': trip_list}
    return render(request, 'subway/index.html', context)

def commutes_index(request):
    trip_list = Trip.objects.order_by('-date')
    context = {'trip_list': trip_list}
    return render(request, 'subway/commutes_index.html', context)

def work_index(request):
    work_trips = Trip.objects.filter(destination__name='work').order_by('-date')
    context = {'work_trips': work_trips}
    return render(request, 'subway/work_trips.html', context)

def home_index(request):
    home_trips = Trip.objects.filter(destination__name='home').order_by('-date')
    context = {'home_trips': home_trips}
    return render(request, 'subway/home_trips.html', context)
