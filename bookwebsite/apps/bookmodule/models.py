from django.db import models

# Create your models here.

# Task 6 Models
class Address(models.Model):
    city = models.CharField(max_length=50)

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=200)  #
    location = models.CharField(max_length=300)  #

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)  #
    DOB = models.DateField(null=True)  #

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)  #[cite: 16]
    price = models.FloatField(default=0.0)  #[cite: 16]
    quantity = models.IntegerField(default=1)  #[cite: 16]
    pubdate = models.DateTimeField()  #[cite: 16]
    rating = models.SmallIntegerField(default=1)  #[cite: 16]
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)  #[cite: 16]
    authors = models.ManyToManyField(Author)  #[cite: 16]

    # حقل عابر (Transient Field) لحساب نسبة التوافر (Task 1)
    @property
    def availability_percentage(self):
        total_qty = Book.objects.aggregate(models.Sum('quantity'))['quantity__sum'] or 1
        return (self.quantity / total_qty) * 100

    def __str__(self):
        return self.title