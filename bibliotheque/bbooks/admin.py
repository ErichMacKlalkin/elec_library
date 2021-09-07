from django.contrib import admin

from .models import Author,Book

class BkAdmin(admin.ModelAdmin):
    list_display = ('name','language')
    list_display_links = ('name','language')
    search_fields = ('name','language')



class BkkAdmin(admin.ModelAdmin):
    list_display = ('title','price')
    list_display_links = ('title','price')
    search_fields = ('title','price')


admin.site.register(Author,BkAdmin)

admin.site.register(Book,BkkAdmin)