from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('api/data/', views.getData, name='api-data'),
    path('<slug:year>/<slug:condition>', views.Graph.as_view(), name='graph')
    # path('api/data/country', views.getCountryData, name='api-country-data'),
]