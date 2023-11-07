from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Жанры книг
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Введите жанр книги', verbose_name='Жанр книги')
    def __str__(self) -> str:
        return self.name
    
# Языки книги
class Language(models.Model):
    name = models.CharField(max_length=20, help_text='Введите язык книги', verbose_name='Язык книги')
    def __str__(self) -> str:
        return self.name

# Издательство
class Publisher(models.Model):
    name = models.CharField(max_length=20, help_text='Введите название издательства', verbose_name='Издательство')
    def __str__(self) -> str:
        return self.name
    
# Авторы
class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text='Введите имя автора', verbose_name='Имя автора')
    last_name = models.CharField(max_length=100, help_text='Введите фамилию автора', verbose_name='Фамилия автора')
    date_of_birth = models.DateField(help_text='Введите дату рождения', verbose_name='Дата рождения', null=True, blank=True)
    about = models.TextField(help_text='Введите сведения об авторе', verbose_name='Сведения об авторе')
    photo = models.ImageField(upload_to='images', help_text='Введите фото автора', verbose_name='Фото автора', null=True, blank=True)
    def __str__(self) -> str:
        return self.last_name
    
# Книги
class Book(models.Model):
    title = models.CharField(max_length=200, help_text='Введите название книги', verbose_name='Название книги')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, help_text='Выберите жанр книги', verbose_name='Жанр книги', null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, help_text='Выберите язык книги', verbose_name='Язык книги', null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, help_text='Выберите издателя книги', verbose_name='Издатель книги', null=True)
    years = models.CharField(max_length=4, help_text='Введите год издания', verbose_name='Год издания')
    author = models.ManyToManyField('Author', help_text='Выберите автора (авторов) книги', verbose_name='Автор (авторы) книги')
    summary = models.TextField(max_length=1000, help_text='Введите краткое описание книги', verbose_name='Аннотация книги')
    isbn = models.CharField(max_length=13, help_text='Должно содержать 13 символов', verbose_name='ISBN книги')
    price = models.DecimalField(decimal_places=2, max_digits=7, help_text='Введите ценуу книги', verbose_name='Цена (руб.)')
    photo = models.ImageField(upload_to='images', help_text='Введите изобразжение книги', verbose_name='Изображение обложки')
    
    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])
    
    display_author.short_description = 'Авторы'

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
# Состояние экземпляра книги
class Status(models.Model):
    name = models.CharField(max_length=20, help_text='Введите статус экземпляра книги', verbose_name='Статус экземпляра книги')
    def __str__(self) -> str:
        return self.name
    
# Экземпляр книги
class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True, help_text='Введите инвентарный номер экзепляра', verbose_name='Инвентарный номер')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True, help_text='Изменить состояние экземпляра', verbose_name='Статус экземпляра книги')
    due_back = models.DateField(null=True, blank=True, help_text='Введите конец срока статуса', verbose_name='Дата окончания статуса')
    borrowed = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Заказчик', help_text='Выберите заказчика книги')
    objects = models.Manager

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    class Meta:
        ordering = ['due_back']
    
    def __str__(self) -> str:
        return '%s %s %s' % (self.inv_nom, self.book, self.status)
    
