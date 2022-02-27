from django.shortcuts import render

from app.models import Category, Image, Location

# Create your views here.
def index(request):
    categories = Category.get_categories(5)
    locations = Location.get_locations(5)
    images = Image.get_all_images()
    return render(request, 'index.html', {'locations': locations, 'categories': categories, 'images':images})