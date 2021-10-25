from django.urls import path
from . import views
app_name = 'rota'
urlpatterns = [
    path('livro_list/',views.livro_list,name='listar_livros'),
    path('livro_new/',views.livro_new, name='livro_new'),
    path('livro_edit/<int:pk>',views.livro_edit, name='livro_edit'),
    path('livro_remove/<int:pk>',views.livro_remove,name ='livro_remove'),
]