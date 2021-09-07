from django.urls import path

from .views import index,BookCreateView,AuthorCreateView,BookUpdateView,BookDeleteView,AutUpdateView,AutDeleteView,SearchResultsView,HomePageView

urlpatterns = [

    path('',index),
    path('/add_book/',BookCreateView.as_view(),name='addbook'),
    path('/add_aut/',AuthorCreateView.as_view(),name='addauthor'),
    path('<int:pk>/delete_book/',BookDeleteView.as_view(),name='delbook'),
    path('<int:pk>/update_book/',BookUpdateView.as_view(),name='upbook'),
    path('<int:pk>/delete_author/',AutDeleteView.as_view(),name='delauthor'),
    path('<int:pk>/update_author/',AutUpdateView.as_view(),name='upauthor'),
    path('/search/', SearchResultsView.as_view(), name='search_results'),
    path('/search_field/', HomePageView.as_view(), name='search_field')
]

