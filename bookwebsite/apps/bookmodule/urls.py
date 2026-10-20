from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="books.index"),
    path('index2/<val1>/', views.index2),
    path('<int:bookId>/', views.viewbook),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links_view, name='links'),
    path('html5/text/formatting', views.text_formatting_view, name='text_formatting'),
    path('html5/listing', views.listing_view, name='listing'),
    path('html5/tables', views.tables_view, name='tables'),
    path('search', views.search_books, name='books.search'),
    path('simple/query', views.simple_query, name='books.simple_query'),
    path('complex/query', views.complex_query, name='books.complex_query'),
    path('lab8/task1', views.task1, name='lab8.task1'),
    path('lab8/task2', views.task2, name='lab8.task2'),
    path('lab8/task3', views.task3, name='lab8.task3'),
    path('lab8/task4', views.task4, name='lab8.task4'),
    path('lab8/task5', views.task5, name='lab8.task5'),
    path('lab8/task7', views.task7, name='lab8.task7'),
]
