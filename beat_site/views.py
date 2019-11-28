from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Country
import csv
from django.http import JsonResponse
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



def get_z_array(self, **kwargs):
    return []

class Graph(TemplateView):
    model = Country
    template_name = 'beat_site/graph.html'

    def get_context_data(self, **kwargs):
        context = super(Graph, self).get_context_data(**kwargs)
        context['year'] = kwargs['year']
        context['condition'] = kwargs['condition']
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
            year = request.POST.get('year')
            condition = slugify(request.POST.get('condition'))
            return redirect(reverse('graph', args=(year,condition)))


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
