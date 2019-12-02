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
import numpy as np
from scipy import stats
import scipy

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

def getIndex(entry):
    if entry <= 10:
        return 0
    elif entry > 10 and entry <= 20 :
        return 1
    elif entry > 20 and entry <= 30 :
        return 2
    elif entry > 30 and entry <= 40 :
        return 3
    elif entry > 40 and entry <= 50 :
        return 4
    elif entry > 50 and entry <= 60 :
        return 5
    elif entry > 60 and entry <= 70 :
        return 6
    elif entry > 70 and entry <= 80 :
        return 7
    elif entry > 80 and entry <= 90 :
        return 8
    elif entry > 90 and entry <= 100 :
        return 9
    elif entry > 100 and entry <= 110 :
        return 10
    elif entry > 110 and entry <= 120 :
        return 11
    elif entry > 120 and entry <= 130 :
        return 12
    elif entry > 130 and entry <= 140 :
        return 13
    elif entry > 140 and entry <= 150 :
        return 14
    elif entry > 150 and entry <= 160 :
        return 15
    elif entry > 160 and entry <= 170 :
        return 16
    elif entry > 170 and entry <= 180 :
        return 17
    elif entry > 180 and entry <= 190 :
        return 18
    elif entry > 190 and entry <= 200 :
        return 19
    elif entry > 200:
        return 20

def UpdateDist(request):
    year_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sample_data = []
    if request.GET.get('condition') == 'gdp':
        min_value = float(request.GET.get('min', None)) * 1000000000
        max_value = float(request.GET.get('max', None)) * 1000000000
        year = request.GET.get('year', None)
        print(year)
        if year != 'all':
            queryset = Country.objects.filter(gdp__range=(min_value, max_value), year=year).values()
        else:
            queryset = Country.objects.filter(gdp__range=(min_value, max_value)).values()
        data = list(queryset)

        for country in data:
            entry = country['rate']
            sample_data.append(entry)
            #Organize so that we can graph distribution
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


    norm_mu, norm_sig, norm_likelihood = normal_mle(sample_data, year_data)
    poiss_mu, poiss_likelihood = poisson_mle(sample_data, year_data)
    pareto_a = pareto_mle(sample_data)
    poiss_dist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    norm_dist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pareto_dist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    trials = 1000

    for i in range(trials):
        entry = np.random.poisson(poiss_mu)
        poiss_dist[getIndex(entry)] += 1

    for i in range(trials):
        entry = np.random.normal(norm_mu, norm_sig)
        norm_dist[getIndex(entry)] += 1

    for i in range(trials):
        entry = np.random.pareto(pareto_a)
        pareto_dist[getIndex(entry)] += 1


    pdf_data = [value / sum(year_data) for value in year_data]
    poiss_dist = [value / sum(poiss_dist) for value in poiss_dist]
    norm_dist = [value / sum(norm_dist) for value in norm_dist]
    pareto_dist = [value / sum(pareto_dist) for value in pareto_dist]


    return JsonResponse({'data':pdf_data,
                        'poiss_pdf':poiss_dist,
                        'poiss_lambda':poiss_mu,
                        'norm_pdf':norm_dist,
                        'pareto_pdf':pareto_dist})


def pareto_mle(sample_data):
    n = len(sample_data)
    p_sum= 0
    k = min(sample_data)
    for data in sample_data:
        p_sum += math.log(data / k)
    print(n / p_sum)
    return n / p_sum

def poisson_mle(sample_data, year_data):
    data_sum = 0
    poiss_pdf = []
    likelihood = 1
    for i in range(len(year_data)):
        data_sum += year_data[i] * (i *10)

    lamb = data_sum / sum(year_data)

    for i in range(len(year_data)):
       poiss_pdf.append(stats.poisson(lamb).pmf(i*10))

    for data in sample_data:
        likelihood *= stats.poisson(lamb).pmf(data)

    return lamb, likelihood


def normal_mle(sample_data, year_data):
    # data_sum = 0
    # for i in range(len(year_data)):
    #     data_sum += year_data[i] * (i *10)
    # mu = data_sum / sum(year_data)
    mu = np.mean(sample_data)
    sig = 0
    likelihood = 1
    norm_pdf = []
    for data in sample_data:
        sig += ((data - mu)**2)
    sig /= len(sample_data)

    for data in sample_data:
        likelihood *= stats.norm(mu, sig).pdf(data)

    # expected_values = []
    # for i in range(len(year_data)):
    #     data_point = stats.norm(mu, sig).pdf((i * 10) + 5)
    #     expected_values.append(data_point)

    # observed_values=scipy.array(year_data)

    # print(stats.chisquare(observed_values, f_exp=expected_values))

    for i in range(len(year_data)):
       norm_pdf.append(stats.norm(mu, sig).pdf(i*10))


    return mu, sig, likelihood


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
