import csv

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from app import settings

with open(settings.BUS_STATION_CSV, encoding='cp1251') as csvfile:
    reader = csv.DictReader(csvfile)
    reader = list(reader)


def index(request):
    return HttpResponseRedirect(reverse('bus_stations') + '?page=1')


def bus_stations(request):
    paginator = Paginator(reader, 10)
    page = request.GET.get('page')
    buses = paginator.get_page(page)
    prev_page_url, next_page_url = None, None
    if buses.has_previous():
        prev_page_url = reverse('bus_stations') + '?page=' + str(buses.previous_page_number())
    if buses.has_next():
        next_page_url = reverse('bus_stations') + '?page=' + str(buses.next_page_number())

    return render_to_response('index.html',
                              context={
        'bus_stations': buses,
        'current_page': page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url}
    )
    # return render_to_response('index.html')