from django.shortcuts import render

from app.models import Category, Location

# Create your views here.
def index(request):
    categories = Category.get_categories(5)
    locations = Location.get_locations(5)
    return render(request, 'index.html', {'locations': locations, 'categories': categories})