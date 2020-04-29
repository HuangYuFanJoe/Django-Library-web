from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)



# Register the admin classes with the associated model
def display_genre(self):
    """Create a string for the Genre. This is required to display genre in Admin."""
    return ', '.join(genre.name for genre in self.genre.all()[:3])
display_genre.short_description = 'Genre'

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', display_genre)
    inlines = [BooksInstanceInline]
"""we can't directly specify the genre field in list_display because it is a ManyToManyField,
   we'll define a display_genre function to get the information as a string"""
admin.site.register(Book, BookAdmin)

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )
