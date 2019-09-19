from django.shortcuts import render
from django.views.generic import ListView
from .models import Country
import csv

class Home(ListView):
    model = Country
    template_name = 'beat_site/home.html'

    # with open('data/countries.csv', encoding="utf-8", errors='ignore') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     iterator = 0
    #     for row in reader:
    #         iterator += 1
    #         try:
    #             Country.objects.get_or_create(name=row['Country Name'], code=row['Country Code'], curr_rate=row['2017'])
    #         except:
    #             print('empty')
