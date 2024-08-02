from django.contrib import admin
from .models import Categories, Author, Book, FileBook, AudioBook, BookAuthor, BookReview


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'categories', 'language', 'pages', 'publication_date', 'isbn', 'price', 'in_sale')
    search_fields = ('title', 'isbn', 'categories__name')
    list_filter = ('categories', 'language', 'in_sale')
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)


@admin.register(FileBook)
class FileBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'book_file')
    search_fields = ('book__title',)
    list_filter = ('book',)


@admin.register(AudioBook)
class AudioBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'audio')
    search_fields = ('book__title',)
    list_filter = ('book',)


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'author')
    search_fields = ('book__title', 'author__first_name', 'author__last_name')
    list_filter = ('book', 'author')


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'stars_given', 'created_at')
    search_fields = ('user__username', 'book__title', 'text')
    list_filter = ('stars_given', 'created_at')
    date_hierarchy = 'created_at'
