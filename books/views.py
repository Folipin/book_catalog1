from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Comment
from .forms import BookForm, CommentForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})

def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    comments = book.comments.all()
    return render(request, 'books/view_book.html', {'book': book, 'comments': comments})

def add_comment(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return redirect('view_book', book_id=book_id)
    else:
        form = CommentForm()
    return render(request, 'books/add_comment.html', {'form': form, 'book': book})