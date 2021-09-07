from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=50,verbose_name='Имя')
    bio = models.TextField(null=True,blank=True,verbose_name='Биография')
    language = models.CharField(max_length=50,null=True,blank=True,verbose_name='Язык')
    books = models.ManyToManyField('Book',blank=True)


    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    author_name = models.CharField(null=True, blank=True,max_length=50,verbose_name='Имя Автора')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'




