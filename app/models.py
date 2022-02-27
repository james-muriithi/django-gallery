from pickle import TRUE
from django.db import models
# cloudinary
from cloudinary.models import CloudinaryField


# location model
class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, null=TRUE, unique=True)

    # save location to database
    def save_location(self):
        self.save()

    # update location
    def update_location(self, name):
        self.name = name
        self.save()

     # delete location from database
    def delete_location(self):
        self.delete()

    @classmethod
    def get_locations(cls, limit=None):
        locations = cls.objects.all()
        return locations if not limit else locations[:limit]

    def __str__(self):
        return self.name


# category model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, null=TRUE, unique=True)

    # save category to database
    def save_category(self):
        self.save()

    # update category
    def update_category(self, name):
        self.name = name
        self.save()

    # delete category from database
    def delete_category(self):
        self.delete()   

    @classmethod
    def get_categories(cls, limit=None):
        categories = cls.objects.all()
        return categories if not limit else categories[:limit]     

    def __str__(self):
        return self.name

    class Meta:    
        verbose_name_plural = "categories"

# Image model
class Image(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    # save image to database
    def save_image(self):
        self.save()


    # update image
    def update_image(self, name, description, location, category):
        self.name = name
        self.description = description
        self.location = location
        self.category = category
        self.save()

    # get all images
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images

    # get image by id
    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.get(id=id)
        return image

    # get images by location
    @classmethod
    def filter_by_location(cls, location):
        images = Image.objects.filter(location__name=location)
        return images

    # get images by category
    @classmethod
    def filter_by_category(cls, category):
        images = Image.objects.filter(category__name=category)
        return images

    # search images
    @classmethod
    def search_image(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images

    # delete image from database
    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.name