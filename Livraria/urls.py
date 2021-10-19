from django.urls import path
from . import views
app_name = 'rota'
urlpatterns = [
    path('livros_list/',views.livro_list,name='listar_livros'),
    path('livro_new/',views.livro_new, name="livro_new"),
]