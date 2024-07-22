from catalog.models import Book, Author, BookInstance, Genre
from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from typing import Any

# Create your views here.

def index(request):
    """View function for home page of site."""
    
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    # Get 5 books containing the title war: queryset = Book.objects.filter(title__icontains='war')[:5] 
    template_name = 'catalog/book_list.html' #Specify your own template name/location

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context.
        context = super().get_context_data(**kwargs)
        # Create any data and add it to the context.
        context['some_data'] = 'This is just some data'
        return context
    
class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'

# If record doesn't exist, use the get_object_or_404()
def book_detail_view(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)

    return render(request, 'catalog/book_detail.html', context={'book': book})