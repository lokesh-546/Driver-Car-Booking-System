from django.urls import path
from . import views

urlpatterns = [
 
path("authors/", views.author_list, name="author_list"),
path("authors/create/", views.author_create, name="author_create"),
path("authors/update/<int:pk>/", views.author_update, name="author_update"),
path("authors/delete/<int:pk>/", views.author_delete, name="author_delete"),
 
path("books/", views.book_list, name="book_list"),
path("books/create/", views.book_create, name="book_create"),
path("books/update/<int:pk>/", views.book_update, name="book_update"),
path("books/delete/<int:pk>/", views.book_delete, name="book_delete"),
 
path("categories/", views.category_list, name="category_list"),
path("categories/create/", views.category_create, name="category_create"),
path("categories/update/<int:pk>/", views.category_update, name="category_update"),
path("categories/delete/<int:pk>/", views.category_delete, name="category_delete"),
]