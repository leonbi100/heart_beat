from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Country
import csv
from django.http import JsonResponse, HttpResponse
import json
from heart_beat.settings import BASE_DIR
import os
from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime
import requests
from django.shortcuts import redirect
from django.urls import reverse
from django.template.defaultfilters import slugify
import math
from django.core import serializers

def get_z_array(self, **kwargs):
    data = []
    result = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    #Filter for correct objects
    if kwargs['year'] != 'all':
        countries = Country.objects.filter(year=kwargs['year'])
    else:
        countries = Country.objects.all()
    if kwargs['condition'] == 'gdp':
        countries = countries.filter(gdp__isnull=False)
    else:
        countries = countries.filter(co2__isnull=False)
    #Put into 2d array
    for country in countries:
        rate = country.rate
        if (isinstance(rate, float) == False):
            continue
        if rate < 10:
            rate = 0
        elif 10 <= rate < 20:
            rate = 1
        elif 20 <= rate < 30:
            rate = 2
        elif 30 <= rate < 40:
            rate = 3
        elif 40 <= rate < 50:
            rate = 4
        elif 50 <= rate < 60:
            rate = 5
        elif 60 <= rate < 70:
            rate = 6
        elif 70 <= rate < 80:
            rate = 7
        elif 80 <= rate < 90:
            rate = 8
        elif 90 <= rate < 100:
            rate = 9
        else:
            rate = 10

        if kwargs['condition'] == 'gdp':
            condition = math.log(country.gdp,10)
            if condition < 7.5:
                condition = 0
            elif 7.5 <= condition < 8:
                condition = 1
            elif 8 <= condition < 8.5:
                condition = 2
            elif 8.5 <= condition < 9:
                condition = 3
            elif 9 <= condition < 9.5:
                condition = 4
            elif 9.5 <= condition < 10:
                condition = 5
            elif 10 <= condition < 10.5:
                condition = 6
            elif 10.5 <= condition < 11:
                condition = 7
            elif 11 <= condition < 11.5:
                condition = 8
            elif 11.5 <= condition < 12:
                condition = 9
            else:
                condition = 10
        else:
            condition = country.co2
            if condition < 2:
                condition = 0
            elif 2 <= condition < 4:
                condition = 1
            elif 4 <= condition < 6:
                condition = 2
            elif 6 <= condition < 8:
                condition = 3
            elif 8 <= condition < 10:
                condition = 4
            elif 10 <= condition < 12:
                condition = 5
            elif 12 <= condition < 14:
                condition = 6
            elif 14 <= condition < 16:
                condition = 7
            elif 16 <= condition < 18:
                condition = 8
            elif 18 <= condition < 20:
                condition = 9
            else:
                condition = 10
        
        data.append((rate, condition))

        for pair in data:
            result[pair[0]][pair[1]] += 1

    for line in result:
        print(line)
    return result

def UpdateDist(request):
    min_value = int(request.GET.get('min', None)) * 1000000000
    max_value = int(request.GET.get('max', None)) * 1000000000
    year = request.GET.get('year', None)
    print(year)
    if year != 'all':
        queryset = Country.objects.filter(gdp__range=(min_value, max_value), year=year).values()
    else:
        queryset = Country.objects.filter(gdp__range=(min_value, max_value)).values()
    data = list(queryset)
    year_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for country in data:
        entry = country['rate']
        if entry <= 10:
            year_data[0] += 1
        elif entry > 10 and entry <= 20 :
            year_data[1] += 1
        elif entry > 20 and entry <= 30 :
            year_data[2] += 1
        elif entry > 30 and entry <= 40 :
            year_data[3] += 1
        elif entry > 40 and entry <= 50 :
            year_data[4] += 1
        elif entry > 50 and entry <= 60 :
            year_data[5] += 1
        elif entry > 60 and entry <= 70 :
            year_data[6] += 1
        elif entry > 70 and entry <= 80 :
            year_data[7] += 1
        elif entry > 80 and entry <= 90 :
            year_data[8] += 1
        elif entry > 90 and entry <= 100 :
            year_data[9] += 1
        elif entry > 100 and entry <= 110 :
            year_data[10] += 1
        elif entry > 110 and entry <= 120 :
            year_data[11] += 1
        elif entry > 120 and entry <= 130 :
            year_data[12] += 1
        elif entry > 130 and entry <= 140 :
            year_data[13] += 1
        elif entry > 140 and entry <= 150 :
            year_data[14] += 1
        elif entry > 150 and entry <= 160 :
            year_data[15] += 1
        elif entry > 160 and entry <= 170 :
            year_data[16] += 1
        elif entry > 170 and entry <= 180 :
            year_data[17] += 1
        elif entry > 180 and entry <= 190 :
            year_data[18] += 1
        elif entry > 190 and entry <= 200 :
            year_data[19] += 1      
        elif entry > 200:
            year_data[20] += 1
    return JsonResponse({'data':year_data})

class Graph(TemplateView):
    model = Country
    template_name = 'beat_site/graph.html'

    def get_context_data(self, **kwargs):
        context = super(Graph, self).get_context_data(**kwargs)
        context['year'] = kwargs['year']
        if kwargs['year'] != 'all':
            context['next_year'] = str(int(kwargs['year']) + 1)
            context['prev_year'] = str(int(kwargs['year']) - 1)
        context['condition'] = kwargs['condition']
        context['z_array'] = get_z_array(self, **kwargs)
        return context

class Home(ListView):
    model = Country
    template_name = 'beat_site/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['range'] = range(1960,2018)
        return context

    def post(self, request):
        if request.method == 'POST':
            year = slugify(request.POST.get('year'))
            condition = slugify(request.POST.get('condition'))
            return redirect(reverse('graph', args=(condition, year)))


def getData(request, *args, **kwargs):
    json_data = open(os.path.join(BASE_DIR, 'beat_site/static/beat_site/countries.json'))
    data = json.load(json_data)
    json_data.close()
    return JsonResponse(data, safe=False)

# def get_topographical_3D_surface_plot():
#     raw_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

#     data = [go.Surface(z=raw_data.as_matrix())]

#     layout = go.Layout(
#         autosize=False,
#         width=500,
#         height=500,
#         margin=dict(
#             l=65,
#             r=50,
#             b=65,
#             t=90
#             )
#         )
#     fig = go.Figure(data=data, layout=layout)
#     plot_div = plot(fig, output_type='div',filename='elevations-3d-surface')

#     return plot_div

# def getCountryData(request, *args, **kwargs):
#     json_data = open(os.path.join(BASE_DIR, 'beat_site/static/beat_site/countries.json'))
#     data = json.load(json_data)
#     json_data.close()
#     return JsonResponse(data, safe=False)
