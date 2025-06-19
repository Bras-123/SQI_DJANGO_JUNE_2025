from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Review
from .forms import ReviewForm

# reviews/views.py

def book_list(request):
    """View to display a list of all books."""
    books = Book.objects.all().order_by('title')
    return render(request, 'reviews/book_list.html', {'books': books})

def book_detail(request, pk):
    """
    View for a single book's detail page.
    Handles both displaying book details and submitting a new review using forms.Form.
    """
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(
                book=book,
                reviewer_name=form.cleaned_data['reviewer_name'],
                rating=form.cleaned_data['rating'],
                comment=form.cleaned_data['comment']
            )
            return redirect('book_detail', pk=book.pk)
    else:
        form = ReviewForm()
        
    reviews = book.reviews.all().order_by('-created_at')

    context = {
        'book': book,
        'reviews': reviews,
        'form': form,
    }

    return render(request, 'reviews/book_detail.html', context)