from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg

# Create your views here.

from .models import Book

def index(request):
    books = Book.objects.all().order_by("title") # to order by descending order use "-title"
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating")) # rating__avg, rating_min
    context = {
        "books": books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating
    }
    return render(request, "book_outlet/index.html", context=context)

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    # book = get_object_or_404(Book, pk=id)
    book = get_object_or_404(Book, slug=slug)
    context = {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    }

    return render(request, "book_outlet/book_details.html", context=context)