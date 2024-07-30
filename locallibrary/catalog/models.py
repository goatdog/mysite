from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .constants import LOAN_STATUS
from datetime import date
import uuid



# Create your models here.
class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text=_('Enter a book genre (e.g.Science Fiction)'))
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class Language(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text=_('Enter a language (e.g.English)'))
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class Book(models.Model):
    """Models representing a book."""
    title = models.CharField(max_length=200)

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    
    summary = models.TextField(max_length=1000, help_text=_("Enter a brief description of the book"))
    isbn = models.CharField("ISBN", max_length=13, unique=True, help_text=_('13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'))

    genre = models.ManyToManyField(Genre, help_text=_("Select a genre for this book"))

    language = models.ManyToManyField(Language, help_text=_("Select a genre for this book"))

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])
    
class BookInstance(models.Model):
    """Models representing a specific copy of a book (that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text=_('Unique ID for this particular book across whole library'))
    book = models.ForeignKey('Book', on_delete=models.RESTRICT)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text=_('Book Availability')
    )

    class Meta:
        ordering = ['due_back']
        permissions = (
            ("can_mark_returned", "Set book as returned"), 
        )
    
    def __str__(self):
        """String for representing the Model object."""
        return f"{self.id} ({self.book.title})"
    
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
    
class Author(models.Model):
    """Model representing an author."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Model object."""
        return f"{self.last_name}, {self.first_name}"
    
    def save(self, *args, **kwargs):
        if (self.date_of_death is not None) and (self.date_of_birth is not None) and self.date_of_death <= self.date_of_birth:
            raise ValidationError("Date of birth cannot be greater or equal than date of death")
        super().save(*args, **kwargs)
    
