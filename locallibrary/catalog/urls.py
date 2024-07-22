from django.urls import path, include
from . import views

# Advanced path matching: 
# - Use regular expression, for example: re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
# - Pass additional options in URL maps: use dictionary, for example: path('myurl/<int:fish>', views.my_view, {'my_template_name': 'some_path'}, name='aurl'),

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]

