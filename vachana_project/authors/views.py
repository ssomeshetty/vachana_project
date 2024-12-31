# authors/views.py
from django.shortcuts import render, get_object_or_404
from .models import Author

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'authors/author_detail.html', {'author': author})
