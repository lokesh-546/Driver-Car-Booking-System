from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

 
# AUTHOR  
 
def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("author_list")
    else:
        form = AuthorForm()

    return render(request, "author_form.html", {"form": form})

def author_list(request):
    authors = Author.objects.all()
    return render(request, "author_list.html", {"authors": authors})

def author_update(request, id):
    author = get_object_or_404(Author, pk=id)

    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect("author_list")
    else:
        form = AuthorForm(instance=author)

    return render(request, "author_form.html", {"form": form})


def author_delete(request, id):
    author = get_object_or_404(Author, pk=id)
    author.delete()
    return redirect("author_list")
 
# CATEGORY 

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm()

    return render(request, "category_form.html", {"form": form})
 
def category_list(request):
    categories = Category.objects.all()
    return render(request, "category_list.html", {"categories": categories})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm(instance=category)

    return render(request, "category_form.html", {"form": form})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("category_list")

# BOOK 
 
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    return render(request, "book_form.html", {"form": form})

def book_list(request):
    books = Book.objects.select_related("author")
    return render(request, "book_list.html", {"books": books})
 
def book_update(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    return render(request, "book_form.html", {"form": form})
 
def book_delete(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    return redirect("book_list")
