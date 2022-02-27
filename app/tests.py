from django.test import TestCase
from app.models import Location, Category, Image

# Create your tests here.

# location model tests
class LocationTestCase(TestCase):

    def setUp(self):
        """
        Create a location for every test
        """
        Location.objects.create(name="Location 1")

    def test_location_name(self):
        """
        Test if location name is correct
        """
        location = Location.objects.get(name="Location 1")
        self.assertEqual(location.name, "Location 1")

    def test_location_save(self):
        """
        Test if save function works
        """
        location = Location(name='Location', slug='location')
        location.save()
        self.assertEqual(Location.get_location_by_slug('location'), location)

    def test_get_locations(self):      
        """
        Test getting all the locations
        """
        self.assertEqual(Location.get_locations().count(), 1)


# category models test
class CategoryTestCase(TestCase):

    def setUp(self):
        """
        Create a category for before each test
        """
        Category.objects.create(name="Category 1", slug="category-1")

    def test_category_name(self):
        """
        Test that the category name is correct
        """
        category = Category.objects.get(name="Category 1")
        self.assertEqual(category.name, "Category 1")

    def test_category_by_slug(self):
        """
        Test getting category by slug
        """
        category = Category.get_category_by_slug('category-1')
        self.assertEqual(category.slug, 'category-1')


    def test_get_all_categories(self):
        """
        Test getting all categories
        """
        self.assertEqual(Category.get_categories().count(), 1)



# image model tests
class ImageTestCase(TestCase):

    def setUp(self):
        """
        Create a image for testing
        """
        Image.objects.create(
            name="Image 1",
            description="Lorem Ipsum",
            location=Location.objects.create(name="Location 1"),
            category=Category.objects.create(name="Category 1"),
            image="https://google.com/default.jpg"
        )

    def test_image_name(self):
        """
        Test that the image name is correct
        """
        image = Image.objects.get(name="Image 1")
        self.assertEqual(image.name, "Image 1")

    def test_image_description(self):
        """
        Test that the image description is correct
        """
        image = Image.objects.get(name="Image 1")
        self.assertEqual(image.description, "Lorem Ipsum")

    def test_image_location(self):
        """
        Test that the image location is correct
        """
        image = Image.objects.get(name="Image 1")
        self.assertEqual(image.location.name, "Location 1")

    def test_image_category(self):
        """
        Test that the image category is correct
        """
        image = Image.objects.get(name="Image 1")
        self.assertEqual(image.category.name, "Category 1")

    def test_image_image(self):
        """
        Test that the image image is correct
        """
        image = Image.objects.get(name="Image 1")
        self.assertEqual(image.image.url, "https://google.com/default")
