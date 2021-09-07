from django.forms import ModelForm

from .models import Book,Author

class BdFormBook(ModelForm):
    class Meta:
        model = Book
        fields = ('title','content','price','author_name')

class BdFormAuthor(ModelForm):
    class Meta:
        model = Author
        fields = ('name','bio','language')


