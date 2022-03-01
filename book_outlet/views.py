from django.shortcuts import get_object_or_404, render
from django.http import Http404

# Create your views here.

from .models import Book

def index(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "book_outlet/index.html", context=context)

def book_detail(request, id):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, pk=id)
    context = {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    }
    
    return render(request, "book_outlet/book_details.html", context=context)