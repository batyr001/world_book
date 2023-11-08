from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Book, Author, BookInstance
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView
from .forms import Form_add_author, Form_edit_author
from django.urls import reverse
from django import forms

def index(request):
    text_head = 'На этом сайте вы можете получить книги в электронном виде'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    authors = Author.objects
    num_authors = Author.objects.count()
    #число посещений этого view
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits +1
    context = {
        'text_head':text_head, 
        'books': books,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'authors': authors,
        'num_authors': num_authors,
        'num_visits': num_visits
        }
    return render(request, 'index.html', context)

class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = 'bookinstance_list_borrowed_user.html'
    paginate_by = 10
    def get_queryset(self):
        return BookInstance.objects.filter(
            borrowed = self.request.user).filter(status__exact='2').order_by('due_back')
        
        
class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book_list.html'
    paginate_by = 3

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book_detail.html'

class AuthorListView(ListView):
    model = Author
    paginate_by = 4
    template_name = 'author_list.html'
    

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    
    
def about (request):
    text_head = 'Сведения о компании'
    name = 'ООО Рога и Копыта'
    rab1 = 'Разарботка приложений на основе ИИ'
    rab2 = 'Распознование лиц'
    rab3 = 'Создание графических арт объектов'
    rab4 = 'Создание цифровых книг'
    context = {'text_head': text_head, 'name':name, 'rab1': rab1, 'rab2': rab2, 'rab3': rab3, 'rab4': rab4}
    return render(request, 'about.html', context)

def contact (request):
    text_head = 'Контакты'
    name = 'ООО Рога и Копыта'
    address = 'Бишкек, 5 мкр'
    phone_number = '0-555-222-345'
    email = 'roga@email.com'
    context = {'text_head': text_head, 'name':name, 'address': address, 'pthone_number': phone_number, 'email': email}
    return render(request, 'contact.html', context)        

def edit_authors(request):
    author = Author.objects.all()
    context = {'author': author}
    return render(request, 'edit_authors.html', context)

def add_author(request):
    if request.method == 'POST':
        form = Form_add_author(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            about = form.cleaned_data.get('about')
            photo = form.cleaned_data.get('photo')
            obj = Author.objects.create(
                first_name = first_name,
                last_name = last_name,
                date_of_birth = date_of_birth,
                about = about,
                photo = photo
            )
            obj.save()
            return HttpResponseRedirect(reverse('authors-list'))
    else:
        form = Form_add_author()
        context = {'form': form}
        return render(request, 'authors_add.html', context)
    
 
    
def delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect('/edit_authors/')
    except:
        return HttpResponseNotFound('<h2> Автор не найден </h2>')
    
def edit_author(requrst, id):
    author = Author.objects.get(id=id)
    if requrst.method == 'POST':
        instance = Author.objects.get(pk=id)
        form = Form_edit_author(requrst.POST, requrst.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/edit_authors/')
    else:
        form = Form_edit_author(instance=author)
        content = {'form': form}
        return render(requrst, 'edit_author.html', content)       
    
# вызов страницы для редактирования книг     
def edit_books(request): 
    book = Book.objects.all()
    context = {'book': book}
    return render(request, 'catalog/edit_books.html', context)
  