from .models import Category,Location
def nav_processor(request):
    categories = Category.get_categories(5)
    locations = Location.get_locations(5)

    return {'categories': categories, 'locations': locations, 'categories': categories }