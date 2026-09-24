from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return render(request, "bookmodule/index.html")



def index2(request, val1=0):
  try:
        val1 = int(val1)
        return HttpResponse(f"value1 = {val1}")
  except ValueError:
        return HttpResponse("error,expected val1 to be integer", status=400)


def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2

    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')