from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from users.models import CustomUser

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='authors/')
    about_author = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='books/')
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    pages = models.IntegerField()
    publication_date = models.DateField(default=timezone.now)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_sale = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class FileBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_file = models.FileField(upload_to='book_file/', blank=True, null=True)

    def __str__(self):
        return self.book


class AudioBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    audio = models.FileField(upload_to='audio_books/', blank=True, null=True)

    def __str__(self):
        return self.book


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} by {self.author.first_name} {self.author.last_name}"


class BookReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    stars_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review by {self.user.username} on {self.book.title}"

