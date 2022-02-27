from django.shortcuts import render

from app.models import Category, Image, Location

# Create your views here.
def index(request):
    images = Image.get_all_images()
    return render(request, 'index.html', {'images':images, 'title': 'Home'})

def category(request, category_slug):
    category = Category.get_category_by_slug(category_slug)
    images = Image.filter_by_category(category)
    return render(request, 'gallery.html', {'images':images, 'title': category})

def location(request, location_slug):
    location = Location.get_location_by_slug(location_slug)
    images = Image.filter_by_location(location)
    return render(request, 'gallery.html', {'images':images, 'title': location})    

def search(request):
    q = request.GET['q']
    images = Image.search_image(q)
    title = f'Search results for {q}' 
    return render(request, 'gallery.html', {'images':images, 'title': title})   

