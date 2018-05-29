from django.shortcuts import render
from subway.models import *

# Create your views here.
def index(request):
    trip_list = Trip.objects.order_by('-date')[:10]
    context = {'trip_list': trip_list}
    return render(request, 'subway/index.html', context)
    
    return render(request, 'polls/index.html', context)