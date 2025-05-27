from django.urls import path
from receitas.views import home, sobre, receita

urlpatterns = [
    path('', home),
    path('sobre', sobre),
    path('receita', receita)
]
