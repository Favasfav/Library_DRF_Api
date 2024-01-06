from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

class BookManager(models.Manager):
    def create_book(self, title, publication_date, author_id):
        author=Author.objects.get(id=author_id) 
        if author.book_set.count() >= 5:
            raise ValidationError("An author cant have more than 5 book")
 
        book = self.create(title=title, publication_date=publication_date, author=author)
        return book
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    bio = models.TextField()
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150)
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    objects=BookManager()
    def __str__(self):
        return self.title
