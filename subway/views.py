from django.db.models import Max, Min, Avg
from django.shortcuts import render
from subway.models import Trip

# Create your views here.
def index(request):
    trip_list = Trip.objects.order_by('-date')[:10]
    num_trips = Trip.objects.count()
    short_trip = Trip.objects.aggregate(Min('duration'))
    long_trip = Trip.objects.aggregate(Max('duration'))
    avg_trip = Trip.objects.aggregate(Avg('duration'))
    work_avg = Trip.objects.filter(destination__name='work').aggregate(Avg('duration'))
    home_avg = Trip.objects.filter(destination__name='home').aggregate(Avg('duration'))
    work_count = Trip.objects.filter(destination__name='work').count()
    home_count = Trip.objects.filter(destination__name='home').count()
    context = {
            'trip_list': trip_list,
            'num_trips': num_trips,
            'fast_trip': short_trip['duration__min'],
            'long_trip': long_trip['duration__max'],
            'avg_trip': round(avg_trip['duration__avg'], 3),
            'work_avg': round(work_avg['duration__avg'], 3),
            'home_avg': round(home_avg['duration__avg'], 3),
            'work_count': work_count,
            'home_count': home_count,
            }
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
