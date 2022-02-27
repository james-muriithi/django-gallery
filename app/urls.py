from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('category/<slug:category_slug>', views.category, name='category'),
    path('location/<slug:location_slug>', views.location, name='location'),
    path('search', views.search, name='search')
]
