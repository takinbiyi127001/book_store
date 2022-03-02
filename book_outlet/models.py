import imp
from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

# For a one-to-one rationship between address and author. One address per Author
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=4)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    # Add a nested class to override the plural form of Address(Addresses)
    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(null=True, max_length=100)
    author = models.ForeignKey(Author,  on_delete=models.CASCADE, null=True, related_name="books") # set a pointer(relationship) to the Author class for author
    is_bestselling = models.BooleanField(default=False)
    # Set blank = True or set editable = False for default behaviour of the slug field.
    # Harry potter 1 => harry-potter-1
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) 

    # Override the builtin save method to add slug from title
    # def save(self, *args, **kwargs): # Remove save method as data is prepopulated in the BookAdmin class
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    # Overrite builtin method get_absolute_url
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def __str__(self):
        return f"{self.title} ({self.rating}) {self.author} ({self.is_bestselling}))"