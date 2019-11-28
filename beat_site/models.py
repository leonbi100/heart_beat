from django.db import models
from django.conf import settings
import os.path
import csv

class CountryManager(models.Manager):

    def import_countries(self):
        with open('data/countries.csv', encoding="utf-8", errors='ignore') as csvfile:
            reader = csv.DictReader(csvfile)
            iterator = 0
            for row in reader:
                self.get_or_create(name=row['Country Name'], code=row['Country Code'], curr_rate=row['2017'])
                iterator += 1
                print(row)
        return iterator

class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=5, blank=True)
    curr_rate = models.FloatField(null=True, blank=True)
    gdp = models.FloatField(null=True, blank=True)
    num_smokers = models.FloatField(null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    co2 = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name_plural = 'countries'

    # def save(self, *args, **kwargs):
    #     super(Country, self).save(*args, **kwargs)

    # def get_project_url(self, *args, **kwargs):
    #     return reverse('project-create') + '?country={}'.format(self.id)

