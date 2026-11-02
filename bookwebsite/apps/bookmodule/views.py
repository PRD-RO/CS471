from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.shortcuts import render
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book, Student, Address

from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
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



def links_view(request):
    return render(request, 'bookmodule/links.html')

def text_formatting_view(request):
    return render(request, 'bookmodule/text-formatting.html')

def listing_view(request):
    return render(request, 'bookmodule/listing.html')

def tables_view(request):
    return render(request, 'bookmodule/tables.html')

from django.shortcuts import render


def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]


def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        books = __getBooksList()
        newBooks = []
        
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)
                
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    
    return render(request, 'bookmodule/search.html')



def simple_query(request):
    
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    


#lab 9 
# Task 1: Price <= 50 using Q operator
def task1(request):
    mybooks = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8/task1.html', {'books': mybooks})

# Task 2: Edition > 3 and (title contains 'co' OR author contains 'qu') (تم التعديل إلى 3 و 'co')
def task2(request):
    mybooks = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8/task2.html', {'books': mybooks})

# Task 3: Opposite to Task 2 using ~ (NOT operator)
def task3(request):
    mybooks = Book.objects.filter(
        ~Q(edition__gt=3) & ~(Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8/task3.html', {'books': mybooks})

# Task 4: Order books by title
def task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8/task4.html', {'books': mybooks})

# Task 5: Aggregation functions
def task5(request):
    stats = Book.objects.aggregate(
        count=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8/task5.html', {'stats': stats})

# Task 7: Count students in each city
def task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab8/task7.html', {'cities': cities})


from django.shortcuts import render
from django.db.models import Sum, Avg, Max, Min, Count, Q
from .models import Book, Publisher, Author

# Task 1: List books along with percentage availability using transient field
def lab9_task1(request):
    books = Book.objects.all()  #[cite: 16]
    return render(request, 'bookmodule/lab9/task1.html', {'books': books})

# Task 2: List publishers annotated with their respective total book stock
def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))  #[cite: 16]
    return render(request, 'bookmodule/lab9/task2.html', {'publishers': publishers})

# Task 3: Get oldest book of any of those managed by every publisher
def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_book=Min('book__pubdate'))  #[cite: 16]
    return render(request, 'bookmodule/lab9/task3.html', {'publishers': publishers})

# Task 4: Calculate average, min, and max price of books for each publisher
def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )  #[cite: 16]
    return render(request, 'bookmodule/lab9/task4.html', {'publishers': publishers})

# Task 5: List publishers with a count of highly rated books, with their names and quantity
def lab9_task5(request):
    publishers = Publisher.objects.filter(book__rating__gte=4).annotate(highly_rated_count=Count('book'))  #
    return render(request, 'bookmodule/lab9/task5.html', {'publishers': publishers})

# Task 6: Count of books for each publisher, filter only books with price > 50 and 1 <= quantity < 5
def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        filtered_books_count=Count(
            'book',
            filter=Q(book__price__gt=50) & Q(book__quantity__lt=5) & Q(book__quantity__gte=1)
        )
    )  #
    return render(request, 'bookmodule/lab9/task6.html', {'publishers': publishers})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm  # تأكد من وجوده أو سنقوم بإنشائه بالأسفل

# ==================== Part 1 Views ====================
def lab10_part1_list(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10/part1_list.html', {'books': books})

def lab10_part1_add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('lab10_p1_list')
    return render(request, 'bookmodule/lab10/part1_add.html')

def lab10_part1_edit(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.edition = request.POST.get('edition')
        book.save()
        return redirect('lab10_p1_list')
    return render(request, 'bookmodule/lab10/part1_edit.html', {'book': book})

def lab10_part1_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('lab10_p1_list')


# ==================== Part 2 Views ====================
def lab10_part2_list(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10/part2_list.html', {'books': books})

def lab10_part2_add(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab10_p2_list')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab10/part2_form.html', {'form': form, 'action': 'Add'})

def lab10_part2_edit(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lab10_p2_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab10/part2_form.html', {'form': form, 'action': 'Edit'})

def lab10_part2_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('lab10_p2_list')