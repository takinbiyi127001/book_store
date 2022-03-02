import imp
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    # Set blank = True or set editable = False for default behaviour of the slug field.
    # Harry potter 1 => harry-potter-1
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) 

    # Override the builtin save method to add slug from title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # Overrite builtin method get_absolute_url
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def __str__(self):
        return f"{self.title} ({self.rating}) {self.author} ({self.is_bestselling}))"