from django.shortcuts import render
from .models import Book,Author
from django.views.generic.edit import CreateView
from .forms import BdFormBook,BdFormAuthor
from django.views.generic import UpdateView,DeleteView,ListView,TemplateView
from django.db.models import Q


def index(request):
    bbs = Book.objects.all()
    att = Author.objects.all()
    context = {'bbs': bbs,'att':att}
    return render(request, 'bbooks/basic.html',context)



class BookCreateView(CreateView):
    template_name = 'bbooks/create_book.html'
    form_class = BdFormBook
    success_url = '/bbooks'

class AuthorCreateView(CreateView):
    template_name = 'bbooks/create_aut.html'
    form_class = BdFormAuthor
    success_url = '/bbooks'


class BookUpdateView(UpdateView):
    template_name = 'bbooks/create_book.html'
    model = Book
    success_url = '/bbooks'
    form_class = BdFormBook


class BookDeleteView(DeleteView):
    template_name = 'bbooks/delete.html'
    model = Book
    success_url = '/bbooks'
    form_class = BdFormBook

class AutUpdateView(UpdateView):
    template_name = 'bbooks/create_aut.html'
    model = Author
    success_url = '/bbooks'
    form_class = BdFormAuthor

class AutDeleteView(DeleteView):
    template_name = 'bbooks/delete.html'
    model = Author
    success_url = '/bbooks'
    form_class = BdFormAuthor



class SearchResultsView(ListView):
    model = Author
    template_name = 'bbooks/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(Q(title__icontains=query) | Q(author_name__icontains=query))
        return object_list





class HomePageView(TemplateView):
    template_name = 'bbooks/search_field.html'