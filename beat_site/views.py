from django.shortcuts import render
from django.views.generic import ListView
from .models import Country
import csv
from django.http import JsonResponse

class Home(ListView):
    model = Country
    template_name = 'beat_site/home.html'

def getData(request, *args, **kwargs):
    data = {
        "rates": [64.7, 63.9, 63, 62.2, 61.2, 60.2,
            59, 57.7, 56.3, 54.8, 53.2, 51.5, 49.8, 48,
            46.3, 44.6, 43, 41.4, 39.9, 38.4, 37.1, 35.7,
            34.5, 33.4, 32.4, 31.4, 30.6, 29.7, 28.9],
        "labels": ["1990", "1991", "1992", "1993", "1994",
            "1995", "1996", "1997", "1998", "1999", "2000",
            "2000", "2001", "2002", "2003", "2004", "2005",
            "2006", "2007", "2008", "2009", "2010", "2011",
            "2012", "2013", "2014", "2015", "2016", "2017", 
            "2018", "2019"]
    }
    return JsonResponse(data)
